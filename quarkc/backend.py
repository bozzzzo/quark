# Copyright 2015 datawire. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, types, java, python, javascript, ruby, tempfile, logging, inspect
from collections import OrderedDict
from .ast import *
from .compiler import TypeExpr, BUILTIN, BUILTIN_FILE, REFLECT
from .dispatch import *
from .helpers import *

class Backend(object):

    PRETTY_INSTALL = "TBD"
    ext = None
    gen = None

    def __init__(self):
        self.files = OrderedDict()
        self._imports = OrderedDict()
        self.current_file = None
        self.current_package = None
        self.packages = []
        self.definitions = []
        self.names = []
        self.bindings = None
        self.entry = None
        self.dist = None
        self.root = None
        self.roots = None
        self.dependencies = OrderedDict()
        self.log = logging.getLogger("quark.compile")

    def install(self):
        cls = self.__class__.__name__
        pkg = self.packages[0].name

        target = self.install_target()
        if os.path.exists(self.root.url):
            deps = (compiled_quark(self.root.url),)
        else:
            deps = ()
        if not (getattr(self.root, "_modified", False) or
                not is_newer(target, __file__, inspect.getsourcefile(self.gen), *deps)):
            self.log.debug("Skipping %s for %s[%s]", cls, pkg, target)
            return

        self.log.debug("Emitting generated %s for %s", cls, pkg)
        dir = tempfile.mkdtemp(suffix="-%s" % cls,
                               prefix="%s-" % pkg)
        self.write(dir)
        self.log.info("Installing %s %s with %s", cls, pkg, self.PRETTY_INSTALL)
        self.install_command(dir)

    def visit_Root(self, r):
        self.root = r

    def visit_DistUnit(self, du):
        self.dist = du

    def visit_Dependency(self, dep):
        self.dependencies["%s:%s.%s-%s" % (dep.lang, dep.group, dep.artifact, dep.version)] = dep

    def visit_Use(self, use):
        entry = self.roots[use.qualified].files[0]
        name, ver = namever(entry)
        self.dependencies[name] = entry

    def visit_File(self, file):
        if not self.entry and not is_meta(file):
            self.entry = file

    def visit_Class(self, cls):
        self.definitions.append(cls)

    def visit_Primitive(self, p):
        pass

    def visit_Function(self, f):
        if not isinstance(f, Method):
            self.definitions.append(f)

    def visit_Package(self, p):
        self.packages.append(p)
        self.definitions.append(p)

    def setfile(self, fname, maker):
        self.current_file = fname
        if fname not in self._imports:
            self._imports[fname] = OrderedDict()
        if fname not in self.files:
            self.files[fname] = maker()
            return False
        return True

    def leave_Root(self, r):
        if self.dist:
            self.entry = self.dist.file

        self.main = None
        for d in self.definitions:
            fname = self.file(d)
            if fname is None:
                continue
            self.current_package = d.package
            if self.setfile(fname, lambda: self.make_file(d)):
                self.files[fname] += "\n"
            dfn_code = self.definition(d)
            if dfn_code and d.package is None and d.file.name.endswith(BUILTIN_FILE):
                self.files[fname] += self.gen.comment("BEGIN_BUILTIN") + "\n"
                self.files[fname] += dfn_code
                self.files[fname] += "\n" + self.gen.comment("END_BUILTIN")
            else:
                self.files[fname] += dfn_code

        if self.main:
            self.genmain()

        for name in self.files:
            code = self.files[name]
            # XXX: this is a hack to avoid circularly dependent
            # imports for generated metadata. To fix this properly, we
            # really need to change the import model for python and js
            # to import classes on demand at the point of use rather
            # than into the module/package level scope.
            raw_imports = self._imports[name].keys()
            refimps = filter(lambda x: x[0] == (BUILTIN, REFLECT), raw_imports)
            imports = filter(lambda x: x[0] != (BUILTIN, REFLECT), raw_imports)

            if name.split("/")[0].endswith("_md"):
                headimps = self.genimps(refimps)
                tailimps = self.genimps(imports)
            else:
                headimps = self.genimps(refimps + imports)
                tailimps = self.genimps([])

            if headimps: code.head += headimps + "\n\n"
            if tailimps: code.tail += "\n\n" + tailimps

            content = str(code)
            if content[-1:] != "\n": content += "\n"
            self.files[name] = content

    def genmain(self):
        self.current_package = None
        name, ver = namever(self.entry)
        fname = self.gen.main_file(self.gen.name(name))
        self.setfile(fname, lambda: self.gen.make_main_file(self.gen.name(name)))
        path = self.add_import(self.main)
        self.files[fname] += self.gen.main(path, self.name(self.main.name))

    def genimps(self, imps):
        imps = [self.gen.import_(pkg, org, dep) for (pkg, org, dep) in imps]
        return "\n".join(filter(lambda x: x is not None, imps))

    def add_import(self, obj):
        imports = self._imports[self.current_file]
        pkg = tuple(self.package(obj))
        if self.current_package:
            org = tuple(self.package(self.current_package))
        else:
            org = ()
        if pkg != org:
            if obj.root != self.root:
                dep, ver = namever(obj.file)
            else:
                dep = None
            imports[(pkg, org, dep)] = True
        return list(self.qualify(pkg, org))

    @overload(Class)
    def file(self, cls):
        return self.gen.class_file(self.package(cls), self.name(cls.name), self.fname(cls))

    @overload(Function)
    def file(self, fun):
        return self.gen.function_file(self.package(fun), self.name(fun.name), self.fname(fun))

    @overload(Package)
    def file(self, pkg):
        return self.gen.package_file(self.package(pkg.package), self.name(pkg.name), self.fname(pkg))

    def fname(self, obj):
        return os.path.splitext(os.path.basename(obj.file.name))[0]

    @overload(Class)
    def make_file(self, cls):
        return self.gen.make_class_file(self.package(cls), self.name(cls.name))

    @overload(Function)
    def make_file(self, fun):
        return self.gen.make_function_file(self.package(fun), self.name(fun.name), mdroot(self.entry))

    @overload(Package)
    def make_file(self, pkg):
        return self.gen.make_package_file(self.package(pkg.package), self.name(pkg.name))

    def write(self, target):
        if not os.path.exists(target):
            os.makedirs(target)
        name, version = namever(self.entry)
        packages = OrderedDict()
        for pkg in self.packages:
            lines = []
            readme(pkg, lines)
            packages[tuple(self.package(pkg))] = "\n".join(lines)

        files_to_emit = OrderedDict(self.files)
        for path, content in self.entry.root.included.items():
            if path.endswith(self.ext):
                files_to_emit[path] = content
        deps = []  # List of (group, artifact, version)
        for dep in self.dependencies.values():
            if isinstance(dep, File):
                dep_name, dep_ver = namever(dep)
                deps.append((dep_name, dep_name, dep_ver))
            elif isinstance(dep, Dependency):
                if dep.lang.text == self.ext:
                    deps.append((dep.group, dep.artifact, dep.version))
            else:
                assert False, (dep, type(dep))

        files = self.gen.package(name, version, packages, files_to_emit, deps)
        for name, content in files.items():
            path = os.path.join(target, name)
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
            open(path, "wb").write(content)
            self.log.debug(" wrote %s", path)

    @overload(Package)
    def definition(self, pkg):
        self.current_package = pkg
        for d in pkg.definitions:
            if isinstance(d, Package):
                self.add_import(d)
        return "" # self.doc(pkg)

    def is_entry_package(self, pkg):
        name, ver = namever(pkg)
        return pkg.name.text == name

    @overload(Function)
    def definition(self, fun):
        if fun.body is None: return ""
        prolog = ""
        if fun.name.text == "main" and len(fun.params) == 1 and \
           fun.params[0].resolved.type.name.text == "List":
            if self.is_entry_package(fun.package):
                self.main = fun
                prolog = self.gen.main_prolog()

        return prolog + self.gen.function(self.doc(fun),
                                          self.type(fun.type),
                                          self.name(fun.name),
                                          [self.param(p) for p in fun.params],
                                          self.block(fun.body))

    @overload(Class)
    def definition(self, cls):
        clazz = self.name(cls.name)
        parameters = [self.name(p.name) for p in cls.parameters]
        base = self.type(base_type(cls))
        interfaces = [self.type(t) for t in cls.bases
                      if isinstance(t.resolved.type, (Interface, Primitive))]

        static_fields = []
        fields = []
        methods = []
        constructors = []

        defaulted, self.bindings = get_defaulted_methods(cls)
        for d in cls.definitions + defaulted.values():
            if isinstance(d, Macro): continue
            doc = self.doc(d)
            if isinstance(d, Field):
                fun = self.gen.static_field if d.static else self.gen.field
                holder = static_fields if d.static else fields
                holder.append(fun(doc,
                                  clazz,
                                  self.type(d.type),
                                  self.name(d.name),
                                  self.expr(d.value)))
            elif d.type:
                if d.body:
                    fun = self.gen.static_method if d.static else self.gen.method
                    methods.append(fun(doc,
                                       clazz,
                                       self.type(d.type),
                                       self.name(d.name),
                                       [self.param(p) for p in d.params],
                                       self.block(d.body)))
                else:
                    methods.append(self.gen.abstract_method(doc,
                                                            clazz,
                                                            self.type(d.type),
                                                            self.name(d.name),
                                                            [self.param(p) for p in d.params]))
            else:
                if base and not has_super(d):
                    header = [self.gen.expr_stmt(self.gen.invoke_super(clazz,
                                                                       self.name(base_type(cls).resolved.type.name),
                                                                       []))]
                elif not base:
                    finit = self.gen.field_init()
                    if finit:
                        header = [finit]
                    else:
                        header = None
                else:
                    header = None
                constructors.append(self.gen.constructor(doc,
                                                         clazz,
                                                         [self.param(p) for p in d.params],
                                                         self.block(d.body, header)))

        if not constructors:
            constructors = self.default_constructors(cls)

        return self.gen.clazz(self.doc(cls), is_abstract(cls), clazz, parameters, base,
                              interfaces, static_fields, fields, constructors, methods)

    @overload(Interface)
    def definition(self, iface):
        name = self.name(iface.name)
        parameters = [self.name(p.name) for p in iface.parameters]
        bases = [self.type(t) for t in iface.bases]

        methods = []
        static_fields = []

        for d in iface.definitions:
            if isinstance(d, Field) and d.static:
                static_fields.append(self.gen.static_field(self.doc(d),
                                                           name,
                                                           self.type(d.type),
                                                           self.name(d.name),
                                                           self.expr(d.value)))
            elif isinstance(d, Method):
                methods.append(self.gen.interface_method(self.doc(d),
                                                         name,
                                                         self.type(d.type),
                                                         self.name(d.name),
                                                         [self.param(p) for p in d.params],
                                                         self.block(d.body)))

        return self.gen.interface(self.doc(iface), name, parameters, bases, static_fields,
                                  methods)

    def default_constructors(self, cls):
        name = self.name(cls.name)
        btype = base_type(cls)
        base = btype.resolved.type if btype else None
        cons = base_constructors(cls)
        result = []
        for con in cons:
            params = [self.param(p) for p in con.params]
            args = [self.name(p.name) for p in con.params]
            stmt = self.gen.expr_stmt(self.gen.invoke_super(name, self.name(base.name), args))
            result.append(self.gen.constructor("", name, params, self.gen.block([stmt])))

        if result:
            return result
        elif base:
            body = self.gen.block([self.gen.expr_stmt(self.gen.invoke_super(name, self.name(base.name), []))])
            result.append(self.gen.constructor("", name, [], body))
        else:
            result.append(self.gen.default_constructor(name))

        return result

    def doc(self, obj):
        return self.gen.doc(doc(obj))

    def push(self, env):
        self.names.append(env)

    def pop(self):
        self.names.pop()

    def name(self, n):
        if self.names:
            env = self.names[-1]
            if n.text in env:
                return env[n.text]
        return self.gen.name(n.text)

    def package(self, node):
        if node is None: return []
        if isinstance(node, Package):
            me = self.name(node.name)
            if node.package:
                return self.package(node.package) + [me]
            else:
                return [me]
        elif node.package:
            return self.package(node.package)
        else:
            assert False

    @overload(Type)
    def type(self, t):
        return self.type(t.resolved)

    @overload(TypeExpr)
    def type(self, texpr):
        return self.type(texpr.type, texpr.bindings)

    @overload(Class, dict)
    def type(self, cls, bindings):
        mapping = None
        for a in cls.annotations:
            if a.name.text == "mapping":
                mapping = a
                break
        if mapping:
            path = []
            name = self.expr(mapping.arguments[0])
        else:
            pkg = self.package(cls)
            path = self.add_import(cls)
            name = self.name(cls.name)

        if cls.parameters:
            params = [self.type(bindings[p]) for p in cls.parameters]
        else:
            params = []

        return self.gen.type(path, name, params)

    def qualify(self, package, origin):
        return self.gen.qualify(package, origin)

    @overload(TypeParam)
    def type(self, tparam, bindings):
        if tparam in bindings:
            return self.type(bindings[tparam])
        elif self.bindings and tparam in self.bindings:
            return self.type(self.bindings[tparam])
        else:
            return self.name(tparam.name)

    @overload(types.NoneType)
    def type(self, n):
        return None

    def param(self, p):
        return self.gen.param(self.type(p.type),
                              self.name(p.name),
                              self.expr(p.value))

    def block(self, b, header=None):
        if b is None:
            return header
        else:
            return self.gen.block((header or []) + [self.statement(s) for s in b.statements])

    @overload(Import)
    def statement(self, imp):
        return self.gen.comment(imp.code())

    @overload(Local)
    def statement(self, s):
        return self.gen.local(self.type(s.declaration.type),
                              self.name(s.declaration.name),
                              self.maybe_cast(s.declaration.type, s.declaration.value))

    @overload(ExprStmt)
    def statement(self, s):
        return self.gen.expr_stmt(self.expr(s.expr))

    @overload(Assign)
    def statement(self, ass):
        return self.gen.assign(self.expr(ass.lhs), self.maybe_cast(ass.lhs, ass.rhs))

    @overload(Return)
    def statement(self, ret):
        return self.gen.return_(self.maybe_cast(ret.callable.type, ret.expr))

    @overload(If)
    def statement(self, iff):
        return self.gen.if_(self.expr(iff.predicate),
                            self.block(iff.consequence),
                            self.block(iff.alternative))

    @overload(While)
    def statement(self, wh):
        return self.gen.while_(self.expr(wh.condition), self.block(wh.body))

    @overload(Break)
    def statement(self, brk):
        return self.gen.break_()

    @overload(Continue)
    def statement(self, cnt):
        return self.gen.continue_()

    @overload(Var)
    def expr(self, v):
        return self.var(v.definition, v)

    @overload(Call)
    def expr(self, c):
        type = c.expr.resolved.type
        return self.invoke(type, c.expr, [self.coerce(a) for a in c.args])

    @overload(String)
    def expr(self, s):
        return self.gen.string(s)

    @overload(Number)
    def expr(self, n):
        return self.gen.number(n)

    @overload(Bool)
    def expr(self, b):
        return self.gen.bool_(b)

    @overload(List)
    def expr(self, l):
        return self.gen.list_([self.expr(e) for e in l.elements])

    @overload(Map)
    def expr(self, m):
        return self.gen.map([(self.expr(e.key), self.expr(e.value)) for e in m.entries])

    @overload(Null)
    def expr(self, n):
        return self.gen.null()

    @overload(Native)
    def expr(self, n):
        return "".join([self.expr(c) for c in n.cases])

    @overload(NativeCase)
    def expr(self, nc):
        if nc.name in (None, self.ext):
            return "".join([self.expr(c) for c in nc.children])
        else:
            return ""

    @overload(Fixed)
    def expr(self, f):
        return f.text

    @overload(Attr)
    def expr(self, a):
        type = a.expr.resolved.type
        return self.get(type, a.resolved.type, a.expr, a.attr)

    @overload(Type)
    def expr(self, t):
        return self.type(t)

    @overload(Cast)
    def expr(self, c):
        return self.maybe_cast(c, c.expr)

    @overload(types.NoneType)
    def expr(self, n):
        return None

    @overload(Param)
    def var(self, _, v):
        return self.gen.local_ref(self.name(v.name))

    @overload(Declaration)
    def var(self, _, v):
        return self.gen.local_ref(self.name(v.name))

    @overload(Class)
    def var(self, _, v):
        return self.gen.class_ref(self.name(v.name))

    @overload(Method)
    def var(self, _, v):
        return self.gen.method_ref(self.name(v.name))

    @overload(Field)
    def var(self, f, v):
        if f.static:
            path = self.add_import(f.clazz)
            return self.gen.get_static_field(path, self.name(f.clazz.name), self.name(v.name))
        else:
            return self.gen.field_ref(self.name(v.name))

    @overload(Class, Class)
    def get(self, cls, type, expr, attr):
        f = get_field(cls, attr)
        if f.static:
            path = self.add_import(f.clazz)
            return self.gen.get_static_field(path, self.name(f.clazz.name), self.name(attr))
        else:
            return self.gen.get_field(self.expr(expr), self.name(attr))

    @overload(Class, TypeParam)
    def get(self, cls, type, expr, attr):
        return self.gen.get_field(self.expr(expr), self.name(attr))

    @overload(Class, Method)
    def get(self, cls, type, expr, attr):
        return self.gen.get_method(self.expr(expr), self.name(attr))

    @overload(Package, Package)
    def get(self, pkg, type, expr, attr):
        return self.gen.get_package(self.expr(expr), self.name(attr))

    @overload(Package, Function)
    def get(self, pkg, type, expr, attr):
        return self.gen.get_function(self.expr(expr), self.name(attr))

    @overload(Function)
    def invoke(self, func, expr, args):
        path = self.add_import(func)
        return self.gen.invoke_function(path, self.name(func.name), args)

    @overload(Method, Attr)
    def invoke(self, method, expr, args):
        if isinstance(expr.expr, Super):
            return self.gen.invoke_super_method(self.name(expr.clazz.name),
                                                self.name(expr.expr.resolved.type.name),
                                                self.name(method.name),
                                                args)
        else:
            if method.static:
                path = self.add_import(method.clazz)
                return self.gen.invoke_static_method(path, self.name(method.clazz.name), self.name(method.name), args)
            else:
                return self.gen.invoke_method(self.expr(expr.expr), self.name(method.name), args)

    @overload(Method, Var)
    def invoke(self, method, var, args):
        if method.static:
            path = self.add_import(method.clazz)
            return self.gen.invoke_static_method(path, self.name(method.clazz.name), self.name(method.name), args)
        else:
            return self.gen.invoke_method_implicit(self.name(method.name), args)

    @overload(Class)
    def invoke(self, cls, expr, args):
        cons = constructors(cls)
        con = cons[0] if cons else None
        if isinstance(con, Macro):
            return self.apply_macro(con, expr, args)
        else:
            return self.gen.construct(self.type(expr.resolved), args)

    @overload(Class, Super)
    def invoke(self, cls, sup, args):
        return self.gen.invoke_super(self.name(sup.clazz.name), self.name(cls.name), args)

    @overload(Macro)
    def invoke(self, macro, expr, args):
        return self.apply_macro(macro, expr, args)

    @overload(Expression)
    def coerce(self, expr):
        if expr.coersion:
            if isinstance(expr.coersion, Macro):
                class FakeExpr: pass
                fake = FakeExpr()
                fake.expr = expr
                fake.resolved = expr.coersion.resolved
                return self.apply_macro(expr.coersion, fake, ())
            else:
                return self.gen.invoke_method(self.expr(expr), self.name(expr.coersion.name), [])
        else:
            return self.expr(expr)

    def apply_macro(self, macro, expr, args):
        env = {}
        if macro.clazz and macro.type:
            bindings = expr.resolved.bindings
            for tparam in bindings:
                env[tparam.name.text] = self.type(bindings[tparam])
            # for method macros we use expr to access self
            env["self"] = self.expr(expr.expr)
        idx = 0
        for p in macro.params:
            env[p.name.text] = args[idx]
            idx += 1
        self.push(env)
        try:
            result = self.expr(macro.body)
            return result
        finally:
            self.pop()

    def maybe_cast(self, type, expr):
        if expr is None: return None
        if expr.coersion:
            return self.coerce(expr)
        if type.resolved.assignableFrom(expr.resolved):
            return self.expr(expr)
        else:
            return self.gen.cast(self.type(type.resolved), self.expr(expr))

import command, os, sys, subprocess, json

def call(*command):
    return subprocess.check_output(command, stderr=subprocess.PIPE)

def is_virtual():
    return hasattr(sys, "real_prefix")

def is_root():
    return os.geteuid() == 0

def is_user():
    return not is_virtual() and not is_root()

class Java(Backend):
    PRETTY_INSTALL = "Maven"
    ext = "java"
    gen = java

    def install_target(self):
        name, ver = namever(self.entry)
        return os.path.join(os.environ["HOME"], ".m2/repository", name, name, ver, "%s-%s.jar" % (name, ver))

    def install_command(self, dir):
        command.call_and_show("install", dir, ["mvn", "install"])

    def run(self, name, version, args):
        jar = os.path.join(os.environ["HOME"], ".m2", "repository", name, name, version,
                           "%s-%s.jar" % (name, version))
        os.execlp("java", "java", "-jar", jar, name, *args)

class Python(Backend):
    PRETTY_INSTALL = "PIP"
    ext = "py"
    gen = python

    def install_target(self):
        name, ver = namever(self.entry)
        try:
            output = call("pip", "show", name)
            for line in output.split("\n"):
                if line.startswith("Location: "):
                    return os.path.join(line.split(": ")[1], name)
        except subprocess.CalledProcessError, e:
            pass
        return None

    def install_command(self, dir):
        command.call_and_show("install", dir, ["python", "setup.py", "-q", "bdist_wheel"])
        wheels = [name for name in os.listdir(os.path.join(dir, "dist")) if name.endswith(".whl")]
        for wheel in wheels:
            cmd = ["pip", "install", "--upgrade", "dist/%s" % wheel]
            if is_user(): cmd += ["--user"]
            command.call_and_show("install", dir, cmd)

    def run(self, name, version, args):
        main = self.gen.name(name)
        os.execlp("python", "python", "-c", "import %s; %s.call_main()" % (main, main), name, *args)

class JavaScript(Backend):
    PRETTY_INSTALL = "NPM"
    ext = "js"
    gen = javascript

    def install_target(self):
        name, ver = namever(self.entry)
        try:
            output = call("npm", "ll", "--depth", "0", "--json", name)
            return json.loads(output)["dependencies"][name]["path"]
        except subprocess.CalledProcessError, e:
            pass
        return None

    def install_command(self, dir):
        command.call_and_show("install", ".", ["npm", "install", dir])

    def run(self, name, version, args):
        main = self.gen.name(name)
        os.execlp("node", "node", "-e", 'require("%s").%s.call_main()' % (name, main), name, *args)

class Ruby(Backend):
    PRETTY_INSTALL = "GEM"
    ext = "rb"
    gen = ruby

    def install_target(self):
        name, ver = namever(self.entry)
        try:
            output = call("gem", "which", name)
            return output.strip()
        except subprocess.CalledProcessError, e:
            pass
        return None

    def install_command(self, dir):
        name, ver = namever(self.entry)
        command.call_and_show("install", dir, ["gem", "build", "-q", "%s.gemspec" % name])
        command.call_and_show("install", ".", ["gem", "install", "%s/%s-%s.gem" % (dir, name, ver)])

    def run(self, name, version, args):
        main = self.gen.name(name)
        os.execlp("ruby", "ruby", "-e", "require('%s'); ::Quark.%s.call_main()" % (name, main), name, *args)

from quark_runtime import *

import quark.reflect


class pkg_A_foo_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_A_foo_Method, self).__init__(u"quark.void", u"foo", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).foo();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_A_bar_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_A_bar_Method, self).__init__(u"quark.void", u"bar", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).bar();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_A(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_A, self).__init__(u"pkg.A");
        (self).name = u"pkg.A"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_A_foo_Method(), pkg_A_bar_Method()])

    def construct(self, args):
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_A.singleton = pkg_A()

class pkg_B_bar_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_B_bar_Method, self).__init__(u"quark.void", u"bar", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).bar();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_B(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_B, self).__init__(u"pkg.B");
        (self).name = u"pkg.B"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_B_bar_Method()])

    def construct(self, args):
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_B.singleton = pkg_B()

class pkg_C_foo_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_C_foo_Method, self).__init__(u"quark.void", u"foo", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).foo();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_C(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_C, self).__init__(u"pkg.C");
        (self).name = u"pkg.C"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_C_foo_Method()])

    def construct(self, args):
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_C.singleton = pkg_C()

class pkg_T1_foo_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T1_foo_Method, self).__init__(u"quark.void", u"foo", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).foo();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T1_bar_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T1_bar_Method, self).__init__(u"quark.void", u"bar", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).bar();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T1(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_T1, self).__init__(u"pkg.T1");
        (self).name = u"pkg.T1"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_T1_foo_Method(), pkg_T1_bar_Method()])

    def construct(self, args):
        return pkg.T1()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_T1.singleton = pkg_T1()

class pkg_T2_foo_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T2_foo_Method, self).__init__(u"quark.void", u"foo", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).foo();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T2_bar_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T2_bar_Method, self).__init__(u"quark.void", u"bar", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).bar();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T2(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_T2, self).__init__(u"pkg.T2");
        (self).name = u"pkg.T2"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_T2_foo_Method(), pkg_T2_bar_Method()])

    def construct(self, args):
        return pkg.T2()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_T2.singleton = pkg_T2()

class pkg_T3_foo_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T3_foo_Method, self).__init__(u"quark.void", u"foo", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).foo();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T3_bar_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T3_bar_Method, self).__init__(u"quark.void", u"bar", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).bar();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T3(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_T3, self).__init__(u"pkg.T3");
        (self).name = u"pkg.T3"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_T3_foo_Method(), pkg_T3_bar_Method()])

    def construct(self, args):
        return pkg.T3()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_T3.singleton = pkg_T3()

class pkg_T4_foo_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T4_foo_Method, self).__init__(u"quark.void", u"foo", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).foo();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T4_bar_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T4_bar_Method, self).__init__(u"quark.void", u"bar", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).bar();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T4(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_T4, self).__init__(u"pkg.T4");
        (self).name = u"pkg.T4"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_T4_foo_Method(), pkg_T4_bar_Method()])

    def construct(self, args):
        return pkg.T4()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_T4.singleton = pkg_T4()

class pkg_T5_foo_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T5_foo_Method, self).__init__(u"quark.void", u"foo", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).foo();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T5_bar_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_T5_bar_Method, self).__init__(u"quark.void", u"bar", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).bar();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_T5(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_T5, self).__init__(u"pkg.T5");
        (self).name = u"pkg.T5"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_T5_foo_Method(), pkg_T5_bar_Method()])

    def construct(self, args):
        return pkg.T5()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_T5.singleton = pkg_T5()

class quark_List_quark_String_(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(quark_List_quark_String_, self).__init__(u"quark.List<quark.String>");
        (self).name = u"quark.List"
        (self).parameters = _List([u"quark.String"])
        (self).fields = _List([])
        (self).methods = _List([])

    def construct(self, args):
        return _List()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
quark_List_quark_String_.singleton = quark_List_quark_String_()

class Root(object):
    def _init(self):
        pass
    def __init__(self): self._init()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
Root.pkg_A_md = pkg_A.singleton
Root.pkg_B_md = pkg_B.singleton
Root.pkg_C_md = pkg_C.singleton
Root.pkg_T1_md = pkg_T1.singleton
Root.pkg_T2_md = pkg_T2.singleton
Root.pkg_T3_md = pkg_T3.singleton
Root.pkg_T4_md = pkg_T4.singleton
Root.pkg_T5_md = pkg_T5.singleton

import pkg

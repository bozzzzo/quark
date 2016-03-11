var _qrt = require("builtin/quark_runtime.js");
var builtin = require('builtin').builtin;
exports.builtin = builtin;



// CLASS box_Box_builtin_Object__set_Method

function box_Box_builtin_Object__set_Method() {
    box_Box_builtin_Object__set_Method.super_.call(this, "builtin.void", "set", ["builtin.Object"]);
}
exports.box_Box_builtin_Object__set_Method = box_Box_builtin_Object__set_Method;
_qrt.util.inherits(box_Box_builtin_Object__set_Method, builtin.reflect.Method);

function box_Box_builtin_Object__set_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Box_builtin_Object__set_Method.prototype.__init_fields__ = box_Box_builtin_Object__set_Method__init_fields__;

function box_Box_builtin_Object__set_Method_invoke(object, args) {
    var obj = object;
    (obj).set((args)[0]);
    return null;
}
box_Box_builtin_Object__set_Method.prototype.invoke = box_Box_builtin_Object__set_Method_invoke;

function box_Box_builtin_Object__set_Method__getClass() {
    return null;
}
box_Box_builtin_Object__set_Method.prototype._getClass = box_Box_builtin_Object__set_Method__getClass;

function box_Box_builtin_Object__set_Method__getField(name) {
    return null;
}
box_Box_builtin_Object__set_Method.prototype._getField = box_Box_builtin_Object__set_Method__getField;

function box_Box_builtin_Object__set_Method__setField(name, value) {}
box_Box_builtin_Object__set_Method.prototype._setField = box_Box_builtin_Object__set_Method__setField;

// CLASS box_Box_builtin_Object__get_Method

function box_Box_builtin_Object__get_Method() {
    box_Box_builtin_Object__get_Method.super_.call(this, "builtin.Object", "get", []);
}
exports.box_Box_builtin_Object__get_Method = box_Box_builtin_Object__get_Method;
_qrt.util.inherits(box_Box_builtin_Object__get_Method, builtin.reflect.Method);

function box_Box_builtin_Object__get_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Box_builtin_Object__get_Method.prototype.__init_fields__ = box_Box_builtin_Object__get_Method__init_fields__;

function box_Box_builtin_Object__get_Method_invoke(object, args) {
    var obj = object;
    return (obj).get();
}
box_Box_builtin_Object__get_Method.prototype.invoke = box_Box_builtin_Object__get_Method_invoke;

function box_Box_builtin_Object__get_Method__getClass() {
    return null;
}
box_Box_builtin_Object__get_Method.prototype._getClass = box_Box_builtin_Object__get_Method__getClass;

function box_Box_builtin_Object__get_Method__getField(name) {
    return null;
}
box_Box_builtin_Object__get_Method.prototype._getField = box_Box_builtin_Object__get_Method__getField;

function box_Box_builtin_Object__get_Method__setField(name, value) {}
box_Box_builtin_Object__get_Method.prototype._setField = box_Box_builtin_Object__get_Method__setField;

// CLASS box_Box_builtin_Object_

function box_Box_builtin_Object_() {
    box_Box_builtin_Object_.super_.call(this, "box.Box<builtin.Object>");
    (this).name = "box.Box";
    (this).parameters = ["builtin.Object"];
    (this).fields = [new builtin.reflect.Field("builtin.Object", "contents")];
    (this).methods = [new box_Box_builtin_Object__set_Method(), new box_Box_builtin_Object__get_Method()];
}
exports.box_Box_builtin_Object_ = box_Box_builtin_Object_;
_qrt.util.inherits(box_Box_builtin_Object_, builtin.reflect.Class);

function box_Box_builtin_Object___init_fields__() {
    builtin.reflect.Class.prototype.__init_fields__.call(this);
}
box_Box_builtin_Object_.prototype.__init_fields__ = box_Box_builtin_Object___init_fields__;
box_Box_builtin_Object_.singleton = new box_Box_builtin_Object_();
function box_Box_builtin_Object__construct(args) {
    return new box.Box();
}
box_Box_builtin_Object_.prototype.construct = box_Box_builtin_Object__construct;

function box_Box_builtin_Object___getClass() {
    return null;
}
box_Box_builtin_Object_.prototype._getClass = box_Box_builtin_Object___getClass;

function box_Box_builtin_Object___getField(name) {
    return null;
}
box_Box_builtin_Object_.prototype._getField = box_Box_builtin_Object___getField;

function box_Box_builtin_Object___setField(name, value) {}
box_Box_builtin_Object_.prototype._setField = box_Box_builtin_Object___setField;


// CLASS box_Box_builtin_int__set_Method

function box_Box_builtin_int__set_Method() {
    box_Box_builtin_int__set_Method.super_.call(this, "builtin.void", "set", ["builtin.int"]);
}
exports.box_Box_builtin_int__set_Method = box_Box_builtin_int__set_Method;
_qrt.util.inherits(box_Box_builtin_int__set_Method, builtin.reflect.Method);

function box_Box_builtin_int__set_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Box_builtin_int__set_Method.prototype.__init_fields__ = box_Box_builtin_int__set_Method__init_fields__;

function box_Box_builtin_int__set_Method_invoke(object, args) {
    var obj = object;
    (obj).set((args)[0]);
    return null;
}
box_Box_builtin_int__set_Method.prototype.invoke = box_Box_builtin_int__set_Method_invoke;

function box_Box_builtin_int__set_Method__getClass() {
    return null;
}
box_Box_builtin_int__set_Method.prototype._getClass = box_Box_builtin_int__set_Method__getClass;

function box_Box_builtin_int__set_Method__getField(name) {
    return null;
}
box_Box_builtin_int__set_Method.prototype._getField = box_Box_builtin_int__set_Method__getField;

function box_Box_builtin_int__set_Method__setField(name, value) {}
box_Box_builtin_int__set_Method.prototype._setField = box_Box_builtin_int__set_Method__setField;

// CLASS box_Box_builtin_int__get_Method

function box_Box_builtin_int__get_Method() {
    box_Box_builtin_int__get_Method.super_.call(this, "builtin.int", "get", []);
}
exports.box_Box_builtin_int__get_Method = box_Box_builtin_int__get_Method;
_qrt.util.inherits(box_Box_builtin_int__get_Method, builtin.reflect.Method);

function box_Box_builtin_int__get_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Box_builtin_int__get_Method.prototype.__init_fields__ = box_Box_builtin_int__get_Method__init_fields__;

function box_Box_builtin_int__get_Method_invoke(object, args) {
    var obj = object;
    return (obj).get();
}
box_Box_builtin_int__get_Method.prototype.invoke = box_Box_builtin_int__get_Method_invoke;

function box_Box_builtin_int__get_Method__getClass() {
    return null;
}
box_Box_builtin_int__get_Method.prototype._getClass = box_Box_builtin_int__get_Method__getClass;

function box_Box_builtin_int__get_Method__getField(name) {
    return null;
}
box_Box_builtin_int__get_Method.prototype._getField = box_Box_builtin_int__get_Method__getField;

function box_Box_builtin_int__get_Method__setField(name, value) {}
box_Box_builtin_int__get_Method.prototype._setField = box_Box_builtin_int__get_Method__setField;

// CLASS box_Box_builtin_int_

function box_Box_builtin_int_() {
    box_Box_builtin_int_.super_.call(this, "box.Box<builtin.int>");
    (this).name = "box.Box";
    (this).parameters = ["builtin.int"];
    (this).fields = [new builtin.reflect.Field("builtin.int", "contents")];
    (this).methods = [new box_Box_builtin_int__set_Method(), new box_Box_builtin_int__get_Method()];
}
exports.box_Box_builtin_int_ = box_Box_builtin_int_;
_qrt.util.inherits(box_Box_builtin_int_, builtin.reflect.Class);

function box_Box_builtin_int___init_fields__() {
    builtin.reflect.Class.prototype.__init_fields__.call(this);
}
box_Box_builtin_int_.prototype.__init_fields__ = box_Box_builtin_int___init_fields__;
box_Box_builtin_int_.singleton = new box_Box_builtin_int_();
function box_Box_builtin_int__construct(args) {
    return new box.Box();
}
box_Box_builtin_int_.prototype.construct = box_Box_builtin_int__construct;

function box_Box_builtin_int___getClass() {
    return null;
}
box_Box_builtin_int_.prototype._getClass = box_Box_builtin_int___getClass;

function box_Box_builtin_int___getField(name) {
    return null;
}
box_Box_builtin_int_.prototype._getField = box_Box_builtin_int___getField;

function box_Box_builtin_int___setField(name, value) {}
box_Box_builtin_int_.prototype._setField = box_Box_builtin_int___setField;


// CLASS box_Box_builtin_String__set_Method

function box_Box_builtin_String__set_Method() {
    box_Box_builtin_String__set_Method.super_.call(this, "builtin.void", "set", ["builtin.String"]);
}
exports.box_Box_builtin_String__set_Method = box_Box_builtin_String__set_Method;
_qrt.util.inherits(box_Box_builtin_String__set_Method, builtin.reflect.Method);

function box_Box_builtin_String__set_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Box_builtin_String__set_Method.prototype.__init_fields__ = box_Box_builtin_String__set_Method__init_fields__;

function box_Box_builtin_String__set_Method_invoke(object, args) {
    var obj = object;
    (obj).set((args)[0]);
    return null;
}
box_Box_builtin_String__set_Method.prototype.invoke = box_Box_builtin_String__set_Method_invoke;

function box_Box_builtin_String__set_Method__getClass() {
    return null;
}
box_Box_builtin_String__set_Method.prototype._getClass = box_Box_builtin_String__set_Method__getClass;

function box_Box_builtin_String__set_Method__getField(name) {
    return null;
}
box_Box_builtin_String__set_Method.prototype._getField = box_Box_builtin_String__set_Method__getField;

function box_Box_builtin_String__set_Method__setField(name, value) {}
box_Box_builtin_String__set_Method.prototype._setField = box_Box_builtin_String__set_Method__setField;

// CLASS box_Box_builtin_String__get_Method

function box_Box_builtin_String__get_Method() {
    box_Box_builtin_String__get_Method.super_.call(this, "builtin.String", "get", []);
}
exports.box_Box_builtin_String__get_Method = box_Box_builtin_String__get_Method;
_qrt.util.inherits(box_Box_builtin_String__get_Method, builtin.reflect.Method);

function box_Box_builtin_String__get_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Box_builtin_String__get_Method.prototype.__init_fields__ = box_Box_builtin_String__get_Method__init_fields__;

function box_Box_builtin_String__get_Method_invoke(object, args) {
    var obj = object;
    return (obj).get();
}
box_Box_builtin_String__get_Method.prototype.invoke = box_Box_builtin_String__get_Method_invoke;

function box_Box_builtin_String__get_Method__getClass() {
    return null;
}
box_Box_builtin_String__get_Method.prototype._getClass = box_Box_builtin_String__get_Method__getClass;

function box_Box_builtin_String__get_Method__getField(name) {
    return null;
}
box_Box_builtin_String__get_Method.prototype._getField = box_Box_builtin_String__get_Method__getField;

function box_Box_builtin_String__get_Method__setField(name, value) {}
box_Box_builtin_String__get_Method.prototype._setField = box_Box_builtin_String__get_Method__setField;

// CLASS box_Box_builtin_String_

function box_Box_builtin_String_() {
    box_Box_builtin_String_.super_.call(this, "box.Box<builtin.String>");
    (this).name = "box.Box";
    (this).parameters = ["builtin.String"];
    (this).fields = [new builtin.reflect.Field("builtin.String", "contents")];
    (this).methods = [new box_Box_builtin_String__set_Method(), new box_Box_builtin_String__get_Method()];
}
exports.box_Box_builtin_String_ = box_Box_builtin_String_;
_qrt.util.inherits(box_Box_builtin_String_, builtin.reflect.Class);

function box_Box_builtin_String___init_fields__() {
    builtin.reflect.Class.prototype.__init_fields__.call(this);
}
box_Box_builtin_String_.prototype.__init_fields__ = box_Box_builtin_String___init_fields__;
box_Box_builtin_String_.singleton = new box_Box_builtin_String_();
function box_Box_builtin_String__construct(args) {
    return new box.Box();
}
box_Box_builtin_String_.prototype.construct = box_Box_builtin_String__construct;

function box_Box_builtin_String___getClass() {
    return null;
}
box_Box_builtin_String_.prototype._getClass = box_Box_builtin_String___getClass;

function box_Box_builtin_String___getField(name) {
    return null;
}
box_Box_builtin_String_.prototype._getField = box_Box_builtin_String___getField;

function box_Box_builtin_String___setField(name, value) {}
box_Box_builtin_String_.prototype._setField = box_Box_builtin_String___setField;


// CLASS box_Box_box_Box_builtin_int___set_Method

function box_Box_box_Box_builtin_int___set_Method() {
    box_Box_box_Box_builtin_int___set_Method.super_.call(this, "builtin.void", "set", ["box.Box<builtin.int>"]);
}
exports.box_Box_box_Box_builtin_int___set_Method = box_Box_box_Box_builtin_int___set_Method;
_qrt.util.inherits(box_Box_box_Box_builtin_int___set_Method, builtin.reflect.Method);

function box_Box_box_Box_builtin_int___set_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Box_box_Box_builtin_int___set_Method.prototype.__init_fields__ = box_Box_box_Box_builtin_int___set_Method__init_fields__;

function box_Box_box_Box_builtin_int___set_Method_invoke(object, args) {
    var obj = object;
    (obj).set((args)[0]);
    return null;
}
box_Box_box_Box_builtin_int___set_Method.prototype.invoke = box_Box_box_Box_builtin_int___set_Method_invoke;

function box_Box_box_Box_builtin_int___set_Method__getClass() {
    return null;
}
box_Box_box_Box_builtin_int___set_Method.prototype._getClass = box_Box_box_Box_builtin_int___set_Method__getClass;

function box_Box_box_Box_builtin_int___set_Method__getField(name) {
    return null;
}
box_Box_box_Box_builtin_int___set_Method.prototype._getField = box_Box_box_Box_builtin_int___set_Method__getField;

function box_Box_box_Box_builtin_int___set_Method__setField(name, value) {}
box_Box_box_Box_builtin_int___set_Method.prototype._setField = box_Box_box_Box_builtin_int___set_Method__setField;

// CLASS box_Box_box_Box_builtin_int___get_Method

function box_Box_box_Box_builtin_int___get_Method() {
    box_Box_box_Box_builtin_int___get_Method.super_.call(this, "box.Box<builtin.int>", "get", []);
}
exports.box_Box_box_Box_builtin_int___get_Method = box_Box_box_Box_builtin_int___get_Method;
_qrt.util.inherits(box_Box_box_Box_builtin_int___get_Method, builtin.reflect.Method);

function box_Box_box_Box_builtin_int___get_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Box_box_Box_builtin_int___get_Method.prototype.__init_fields__ = box_Box_box_Box_builtin_int___get_Method__init_fields__;

function box_Box_box_Box_builtin_int___get_Method_invoke(object, args) {
    var obj = object;
    return (obj).get();
}
box_Box_box_Box_builtin_int___get_Method.prototype.invoke = box_Box_box_Box_builtin_int___get_Method_invoke;

function box_Box_box_Box_builtin_int___get_Method__getClass() {
    return null;
}
box_Box_box_Box_builtin_int___get_Method.prototype._getClass = box_Box_box_Box_builtin_int___get_Method__getClass;

function box_Box_box_Box_builtin_int___get_Method__getField(name) {
    return null;
}
box_Box_box_Box_builtin_int___get_Method.prototype._getField = box_Box_box_Box_builtin_int___get_Method__getField;

function box_Box_box_Box_builtin_int___get_Method__setField(name, value) {}
box_Box_box_Box_builtin_int___get_Method.prototype._setField = box_Box_box_Box_builtin_int___get_Method__setField;

// CLASS box_Box_box_Box_builtin_int__

function box_Box_box_Box_builtin_int__() {
    box_Box_box_Box_builtin_int__.super_.call(this, "box.Box<box.Box<builtin.int>>");
    (this).name = "box.Box";
    (this).parameters = ["box.Box<builtin.int>"];
    (this).fields = [new builtin.reflect.Field("box.Box<builtin.int>", "contents")];
    (this).methods = [new box_Box_box_Box_builtin_int___set_Method(), new box_Box_box_Box_builtin_int___get_Method()];
}
exports.box_Box_box_Box_builtin_int__ = box_Box_box_Box_builtin_int__;
_qrt.util.inherits(box_Box_box_Box_builtin_int__, builtin.reflect.Class);

function box_Box_box_Box_builtin_int____init_fields__() {
    builtin.reflect.Class.prototype.__init_fields__.call(this);
}
box_Box_box_Box_builtin_int__.prototype.__init_fields__ = box_Box_box_Box_builtin_int____init_fields__;
box_Box_box_Box_builtin_int__.singleton = new box_Box_box_Box_builtin_int__();
function box_Box_box_Box_builtin_int___construct(args) {
    return new box.Box();
}
box_Box_box_Box_builtin_int__.prototype.construct = box_Box_box_Box_builtin_int___construct;

function box_Box_box_Box_builtin_int____getClass() {
    return null;
}
box_Box_box_Box_builtin_int__.prototype._getClass = box_Box_box_Box_builtin_int____getClass;

function box_Box_box_Box_builtin_int____getField(name) {
    return null;
}
box_Box_box_Box_builtin_int__.prototype._getField = box_Box_box_Box_builtin_int____getField;

function box_Box_box_Box_builtin_int____setField(name, value) {}
box_Box_box_Box_builtin_int__.prototype._setField = box_Box_box_Box_builtin_int____setField;


// CLASS box_Crate_builtin_int__set_Method

function box_Crate_builtin_int__set_Method() {
    box_Crate_builtin_int__set_Method.super_.call(this, "builtin.void", "set", ["builtin.int"]);
}
exports.box_Crate_builtin_int__set_Method = box_Crate_builtin_int__set_Method;
_qrt.util.inherits(box_Crate_builtin_int__set_Method, builtin.reflect.Method);

function box_Crate_builtin_int__set_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Crate_builtin_int__set_Method.prototype.__init_fields__ = box_Crate_builtin_int__set_Method__init_fields__;

function box_Crate_builtin_int__set_Method_invoke(object, args) {
    var obj = object;
    (obj).set((args)[0]);
    return null;
}
box_Crate_builtin_int__set_Method.prototype.invoke = box_Crate_builtin_int__set_Method_invoke;

function box_Crate_builtin_int__set_Method__getClass() {
    return null;
}
box_Crate_builtin_int__set_Method.prototype._getClass = box_Crate_builtin_int__set_Method__getClass;

function box_Crate_builtin_int__set_Method__getField(name) {
    return null;
}
box_Crate_builtin_int__set_Method.prototype._getField = box_Crate_builtin_int__set_Method__getField;

function box_Crate_builtin_int__set_Method__setField(name, value) {}
box_Crate_builtin_int__set_Method.prototype._setField = box_Crate_builtin_int__set_Method__setField;

// CLASS box_Crate_builtin_int__get_Method

function box_Crate_builtin_int__get_Method() {
    box_Crate_builtin_int__get_Method.super_.call(this, "builtin.int", "get", []);
}
exports.box_Crate_builtin_int__get_Method = box_Crate_builtin_int__get_Method;
_qrt.util.inherits(box_Crate_builtin_int__get_Method, builtin.reflect.Method);

function box_Crate_builtin_int__get_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Crate_builtin_int__get_Method.prototype.__init_fields__ = box_Crate_builtin_int__get_Method__init_fields__;

function box_Crate_builtin_int__get_Method_invoke(object, args) {
    var obj = object;
    return (obj).get();
}
box_Crate_builtin_int__get_Method.prototype.invoke = box_Crate_builtin_int__get_Method_invoke;

function box_Crate_builtin_int__get_Method__getClass() {
    return null;
}
box_Crate_builtin_int__get_Method.prototype._getClass = box_Crate_builtin_int__get_Method__getClass;

function box_Crate_builtin_int__get_Method__getField(name) {
    return null;
}
box_Crate_builtin_int__get_Method.prototype._getField = box_Crate_builtin_int__get_Method__getField;

function box_Crate_builtin_int__get_Method__setField(name, value) {}
box_Crate_builtin_int__get_Method.prototype._setField = box_Crate_builtin_int__get_Method__setField;

// CLASS box_Crate_builtin_int_

function box_Crate_builtin_int_() {
    box_Crate_builtin_int_.super_.call(this, "box.Crate<builtin.int>");
    (this).name = "box.Crate";
    (this).parameters = ["builtin.int"];
    (this).fields = [new builtin.reflect.Field("box.Box<builtin.Object>", "box"), new builtin.reflect.Field("box.Box<builtin.int>", "ibox")];
    (this).methods = [new box_Crate_builtin_int__set_Method(), new box_Crate_builtin_int__get_Method()];
}
exports.box_Crate_builtin_int_ = box_Crate_builtin_int_;
_qrt.util.inherits(box_Crate_builtin_int_, builtin.reflect.Class);

function box_Crate_builtin_int___init_fields__() {
    builtin.reflect.Class.prototype.__init_fields__.call(this);
}
box_Crate_builtin_int_.prototype.__init_fields__ = box_Crate_builtin_int___init_fields__;
box_Crate_builtin_int_.singleton = new box_Crate_builtin_int_();
function box_Crate_builtin_int__construct(args) {
    return new box.Crate();
}
box_Crate_builtin_int_.prototype.construct = box_Crate_builtin_int__construct;

function box_Crate_builtin_int___getClass() {
    return null;
}
box_Crate_builtin_int_.prototype._getClass = box_Crate_builtin_int___getClass;

function box_Crate_builtin_int___getField(name) {
    return null;
}
box_Crate_builtin_int_.prototype._getField = box_Crate_builtin_int___getField;

function box_Crate_builtin_int___setField(name, value) {}
box_Crate_builtin_int_.prototype._setField = box_Crate_builtin_int___setField;


// CLASS box_Crate_builtin_String__set_Method

function box_Crate_builtin_String__set_Method() {
    box_Crate_builtin_String__set_Method.super_.call(this, "builtin.void", "set", ["builtin.String"]);
}
exports.box_Crate_builtin_String__set_Method = box_Crate_builtin_String__set_Method;
_qrt.util.inherits(box_Crate_builtin_String__set_Method, builtin.reflect.Method);

function box_Crate_builtin_String__set_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Crate_builtin_String__set_Method.prototype.__init_fields__ = box_Crate_builtin_String__set_Method__init_fields__;

function box_Crate_builtin_String__set_Method_invoke(object, args) {
    var obj = object;
    (obj).set((args)[0]);
    return null;
}
box_Crate_builtin_String__set_Method.prototype.invoke = box_Crate_builtin_String__set_Method_invoke;

function box_Crate_builtin_String__set_Method__getClass() {
    return null;
}
box_Crate_builtin_String__set_Method.prototype._getClass = box_Crate_builtin_String__set_Method__getClass;

function box_Crate_builtin_String__set_Method__getField(name) {
    return null;
}
box_Crate_builtin_String__set_Method.prototype._getField = box_Crate_builtin_String__set_Method__getField;

function box_Crate_builtin_String__set_Method__setField(name, value) {}
box_Crate_builtin_String__set_Method.prototype._setField = box_Crate_builtin_String__set_Method__setField;

// CLASS box_Crate_builtin_String__get_Method

function box_Crate_builtin_String__get_Method() {
    box_Crate_builtin_String__get_Method.super_.call(this, "builtin.String", "get", []);
}
exports.box_Crate_builtin_String__get_Method = box_Crate_builtin_String__get_Method;
_qrt.util.inherits(box_Crate_builtin_String__get_Method, builtin.reflect.Method);

function box_Crate_builtin_String__get_Method__init_fields__() {
    builtin.reflect.Method.prototype.__init_fields__.call(this);
}
box_Crate_builtin_String__get_Method.prototype.__init_fields__ = box_Crate_builtin_String__get_Method__init_fields__;

function box_Crate_builtin_String__get_Method_invoke(object, args) {
    var obj = object;
    return (obj).get();
}
box_Crate_builtin_String__get_Method.prototype.invoke = box_Crate_builtin_String__get_Method_invoke;

function box_Crate_builtin_String__get_Method__getClass() {
    return null;
}
box_Crate_builtin_String__get_Method.prototype._getClass = box_Crate_builtin_String__get_Method__getClass;

function box_Crate_builtin_String__get_Method__getField(name) {
    return null;
}
box_Crate_builtin_String__get_Method.prototype._getField = box_Crate_builtin_String__get_Method__getField;

function box_Crate_builtin_String__get_Method__setField(name, value) {}
box_Crate_builtin_String__get_Method.prototype._setField = box_Crate_builtin_String__get_Method__setField;

// CLASS box_Crate_builtin_String_

function box_Crate_builtin_String_() {
    box_Crate_builtin_String_.super_.call(this, "box.Crate<builtin.String>");
    (this).name = "box.Crate";
    (this).parameters = ["builtin.String"];
    (this).fields = [new builtin.reflect.Field("box.Box<builtin.Object>", "box"), new builtin.reflect.Field("box.Box<builtin.int>", "ibox")];
    (this).methods = [new box_Crate_builtin_String__set_Method(), new box_Crate_builtin_String__get_Method()];
}
exports.box_Crate_builtin_String_ = box_Crate_builtin_String_;
_qrt.util.inherits(box_Crate_builtin_String_, builtin.reflect.Class);

function box_Crate_builtin_String___init_fields__() {
    builtin.reflect.Class.prototype.__init_fields__.call(this);
}
box_Crate_builtin_String_.prototype.__init_fields__ = box_Crate_builtin_String___init_fields__;
box_Crate_builtin_String_.singleton = new box_Crate_builtin_String_();
function box_Crate_builtin_String__construct(args) {
    return new box.Crate();
}
box_Crate_builtin_String_.prototype.construct = box_Crate_builtin_String__construct;

function box_Crate_builtin_String___getClass() {
    return null;
}
box_Crate_builtin_String_.prototype._getClass = box_Crate_builtin_String___getClass;

function box_Crate_builtin_String___getField(name) {
    return null;
}
box_Crate_builtin_String_.prototype._getField = box_Crate_builtin_String___getField;

function box_Crate_builtin_String___setField(name, value) {}
box_Crate_builtin_String_.prototype._setField = box_Crate_builtin_String___setField;


// CLASS box_Sack

function box_Sack() {
    box_Sack.super_.call(this, "box.Sack");
    (this).name = "box.Sack";
    (this).parameters = [];
    (this).fields = [new builtin.reflect.Field("box.Box<builtin.int>", "ints")];
    (this).methods = [];
}
exports.box_Sack = box_Sack;
_qrt.util.inherits(box_Sack, builtin.reflect.Class);

function box_Sack__init_fields__() {
    builtin.reflect.Class.prototype.__init_fields__.call(this);
}
box_Sack.prototype.__init_fields__ = box_Sack__init_fields__;
box_Sack.singleton = new box_Sack();
function box_Sack_construct(args) {
    return new box.Sack();
}
box_Sack.prototype.construct = box_Sack_construct;

function box_Sack__getClass() {
    return null;
}
box_Sack.prototype._getClass = box_Sack__getClass;

function box_Sack__getField(name) {
    return null;
}
box_Sack.prototype._getField = box_Sack__getField;

function box_Sack__setField(name, value) {}
box_Sack.prototype._setField = box_Sack__setField;


// CLASS Root
function Root() {
    this.__init_fields__();
}
exports.Root = Root;

function Root__init_fields__() {}
Root.prototype.__init_fields__ = Root__init_fields__;
Root.box_Box_builtin_Object__md = box_Box_builtin_Object_.singleton;
Root.box_Box_builtin_int__md = box_Box_builtin_int_.singleton;
Root.box_Sack_md = box_Sack.singleton;
function Root__getClass() {
    return null;
}
Root.prototype._getClass = Root__getClass;

function Root__getField(name) {
    return null;
}
Root.prototype._getField = Root__getField;

function Root__setField(name, value) {}
Root.prototype._setField = Root__setField;

var box = require('../box/index.js');
exports.box = box;

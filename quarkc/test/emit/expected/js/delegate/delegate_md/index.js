var _qrt = require("quark/quark_runtime.js");
var quark = require('quark').quark;
exports.quark = quark;



// CLASS delegate_Message_encode_Method

function delegate_Message_encode_Method() {
    delegate_Message_encode_Method.super_.call(this, "quark.String", "encode", []);
}
exports.delegate_Message_encode_Method = delegate_Message_encode_Method;
_qrt.util.inherits(delegate_Message_encode_Method, quark.reflect.Method);

function delegate_Message_encode_Method__init_fields__() {
    quark.reflect.Method.prototype.__init_fields__.call(this);
}
delegate_Message_encode_Method.prototype.__init_fields__ = delegate_Message_encode_Method__init_fields__;

function delegate_Message_encode_Method_invoke(object, args) {
    var obj = object;
    return (obj).encode();
}
delegate_Message_encode_Method.prototype.invoke = delegate_Message_encode_Method_invoke;

function delegate_Message_encode_Method__getClass() {
    return null;
}
delegate_Message_encode_Method.prototype._getClass = delegate_Message_encode_Method__getClass;

function delegate_Message_encode_Method__getField(name) {
    return null;
}
delegate_Message_encode_Method.prototype._getField = delegate_Message_encode_Method__getField;

function delegate_Message_encode_Method__setField(name, value) {}
delegate_Message_encode_Method.prototype._setField = delegate_Message_encode_Method__setField;

// CLASS delegate_Message

function delegate_Message() {
    delegate_Message.super_.call(this, "delegate.Message");
    (this).name = "delegate.Message";
    (this).parameters = [];
    (this).fields = [];
    (this).methods = [new delegate_Message_encode_Method()];
}
exports.delegate_Message = delegate_Message;
_qrt.util.inherits(delegate_Message, quark.reflect.Class);

function delegate_Message__init_fields__() {
    quark.reflect.Class.prototype.__init_fields__.call(this);
}
delegate_Message.prototype.__init_fields__ = delegate_Message__init_fields__;
delegate_Message.singleton = new delegate_Message();
function delegate_Message_construct(args) {
    return new delegate.Message();
}
delegate_Message.prototype.construct = delegate_Message_construct;

function delegate_Message__getClass() {
    return null;
}
delegate_Message.prototype._getClass = delegate_Message__getClass;

function delegate_Message__getField(name) {
    return null;
}
delegate_Message.prototype._getField = delegate_Message__getField;

function delegate_Message__setField(name, value) {}
delegate_Message.prototype._setField = delegate_Message__setField;


// CLASS delegate_Ping_encode_Method

function delegate_Ping_encode_Method() {
    delegate_Ping_encode_Method.super_.call(this, "quark.String", "encode", []);
}
exports.delegate_Ping_encode_Method = delegate_Ping_encode_Method;
_qrt.util.inherits(delegate_Ping_encode_Method, quark.reflect.Method);

function delegate_Ping_encode_Method__init_fields__() {
    quark.reflect.Method.prototype.__init_fields__.call(this);
}
delegate_Ping_encode_Method.prototype.__init_fields__ = delegate_Ping_encode_Method__init_fields__;

function delegate_Ping_encode_Method_invoke(object, args) {
    var obj = object;
    return (obj).encode();
}
delegate_Ping_encode_Method.prototype.invoke = delegate_Ping_encode_Method_invoke;

function delegate_Ping_encode_Method__getClass() {
    return null;
}
delegate_Ping_encode_Method.prototype._getClass = delegate_Ping_encode_Method__getClass;

function delegate_Ping_encode_Method__getField(name) {
    return null;
}
delegate_Ping_encode_Method.prototype._getField = delegate_Ping_encode_Method__getField;

function delegate_Ping_encode_Method__setField(name, value) {}
delegate_Ping_encode_Method.prototype._setField = delegate_Ping_encode_Method__setField;

// CLASS delegate_Ping

function delegate_Ping() {
    delegate_Ping.super_.call(this, "delegate.Ping");
    (this).name = "delegate.Ping";
    (this).parameters = [];
    (this).fields = [];
    (this).methods = [new delegate_Ping_encode_Method()];
}
exports.delegate_Ping = delegate_Ping;
_qrt.util.inherits(delegate_Ping, quark.reflect.Class);

function delegate_Ping__init_fields__() {
    quark.reflect.Class.prototype.__init_fields__.call(this);
}
delegate_Ping.prototype.__init_fields__ = delegate_Ping__init_fields__;
delegate_Ping.singleton = new delegate_Ping();
function delegate_Ping_construct(args) {
    return new delegate.Ping();
}
delegate_Ping.prototype.construct = delegate_Ping_construct;

function delegate_Ping__getClass() {
    return null;
}
delegate_Ping.prototype._getClass = delegate_Ping__getClass;

function delegate_Ping__getField(name) {
    return null;
}
delegate_Ping.prototype._getField = delegate_Ping__getField;

function delegate_Ping__setField(name, value) {}
delegate_Ping.prototype._setField = delegate_Ping__setField;


// CLASS delegate_Pong_toString_Method

function delegate_Pong_toString_Method() {
    delegate_Pong_toString_Method.super_.call(this, "quark.String", "toString", []);
}
exports.delegate_Pong_toString_Method = delegate_Pong_toString_Method;
_qrt.util.inherits(delegate_Pong_toString_Method, quark.reflect.Method);

function delegate_Pong_toString_Method__init_fields__() {
    quark.reflect.Method.prototype.__init_fields__.call(this);
}
delegate_Pong_toString_Method.prototype.__init_fields__ = delegate_Pong_toString_Method__init_fields__;

function delegate_Pong_toString_Method_invoke(object, args) {
    var obj = object;
    return (obj).toString();
}
delegate_Pong_toString_Method.prototype.invoke = delegate_Pong_toString_Method_invoke;

function delegate_Pong_toString_Method__getClass() {
    return null;
}
delegate_Pong_toString_Method.prototype._getClass = delegate_Pong_toString_Method__getClass;

function delegate_Pong_toString_Method__getField(name) {
    return null;
}
delegate_Pong_toString_Method.prototype._getField = delegate_Pong_toString_Method__getField;

function delegate_Pong_toString_Method__setField(name, value) {}
delegate_Pong_toString_Method.prototype._setField = delegate_Pong_toString_Method__setField;

// CLASS delegate_Pong_encode_Method

function delegate_Pong_encode_Method() {
    delegate_Pong_encode_Method.super_.call(this, "quark.String", "encode", []);
}
exports.delegate_Pong_encode_Method = delegate_Pong_encode_Method;
_qrt.util.inherits(delegate_Pong_encode_Method, quark.reflect.Method);

function delegate_Pong_encode_Method__init_fields__() {
    quark.reflect.Method.prototype.__init_fields__.call(this);
}
delegate_Pong_encode_Method.prototype.__init_fields__ = delegate_Pong_encode_Method__init_fields__;

function delegate_Pong_encode_Method_invoke(object, args) {
    var obj = object;
    return (obj).encode();
}
delegate_Pong_encode_Method.prototype.invoke = delegate_Pong_encode_Method_invoke;

function delegate_Pong_encode_Method__getClass() {
    return null;
}
delegate_Pong_encode_Method.prototype._getClass = delegate_Pong_encode_Method__getClass;

function delegate_Pong_encode_Method__getField(name) {
    return null;
}
delegate_Pong_encode_Method.prototype._getField = delegate_Pong_encode_Method__getField;

function delegate_Pong_encode_Method__setField(name, value) {}
delegate_Pong_encode_Method.prototype._setField = delegate_Pong_encode_Method__setField;

// CLASS delegate_Pong

function delegate_Pong() {
    delegate_Pong.super_.call(this, "delegate.Pong");
    (this).name = "delegate.Pong";
    (this).parameters = [];
    (this).fields = [];
    (this).methods = [new delegate_Pong_toString_Method(), new delegate_Pong_encode_Method()];
}
exports.delegate_Pong = delegate_Pong;
_qrt.util.inherits(delegate_Pong, quark.reflect.Class);

function delegate_Pong__init_fields__() {
    quark.reflect.Class.prototype.__init_fields__.call(this);
}
delegate_Pong.prototype.__init_fields__ = delegate_Pong__init_fields__;
delegate_Pong.singleton = new delegate_Pong();
function delegate_Pong_construct(args) {
    return new delegate.Pong();
}
delegate_Pong.prototype.construct = delegate_Pong_construct;

function delegate_Pong__getClass() {
    return null;
}
delegate_Pong.prototype._getClass = delegate_Pong__getClass;

function delegate_Pong__getField(name) {
    return null;
}
delegate_Pong.prototype._getField = delegate_Pong__getField;

function delegate_Pong__setField(name, value) {}
delegate_Pong.prototype._setField = delegate_Pong__setField;


// CLASS delegate_Test_bar_Method

function delegate_Test_bar_Method() {
    delegate_Test_bar_Method.super_.call(this, "quark.Object", "bar", ["quark.String", "quark.List<quark.Object>", "quark.List<quark.Object>"]);
}
exports.delegate_Test_bar_Method = delegate_Test_bar_Method;
_qrt.util.inherits(delegate_Test_bar_Method, quark.reflect.Method);

function delegate_Test_bar_Method__init_fields__() {
    quark.reflect.Method.prototype.__init_fields__.call(this);
}
delegate_Test_bar_Method.prototype.__init_fields__ = delegate_Test_bar_Method__init_fields__;

function delegate_Test_bar_Method_invoke(object, args) {
    var obj = object;
    return (obj).bar((args)[0], (args)[1], (args)[2]);
}
delegate_Test_bar_Method.prototype.invoke = delegate_Test_bar_Method_invoke;

function delegate_Test_bar_Method__getClass() {
    return null;
}
delegate_Test_bar_Method.prototype._getClass = delegate_Test_bar_Method__getClass;

function delegate_Test_bar_Method__getField(name) {
    return null;
}
delegate_Test_bar_Method.prototype._getField = delegate_Test_bar_Method__getField;

function delegate_Test_bar_Method__setField(name, value) {}
delegate_Test_bar_Method.prototype._setField = delegate_Test_bar_Method__setField;

// CLASS delegate_Test_foo_Method

function delegate_Test_foo_Method() {
    delegate_Test_foo_Method.super_.call(this, "quark.void", "foo", ["quark.String", "quark.String", "quark.int"]);
}
exports.delegate_Test_foo_Method = delegate_Test_foo_Method;
_qrt.util.inherits(delegate_Test_foo_Method, quark.reflect.Method);

function delegate_Test_foo_Method__init_fields__() {
    quark.reflect.Method.prototype.__init_fields__.call(this);
}
delegate_Test_foo_Method.prototype.__init_fields__ = delegate_Test_foo_Method__init_fields__;

function delegate_Test_foo_Method_invoke(object, args) {
    var obj = object;
    (obj).foo((args)[0], (args)[1], (args)[2]);
    return null;
}
delegate_Test_foo_Method.prototype.invoke = delegate_Test_foo_Method_invoke;

function delegate_Test_foo_Method__getClass() {
    return null;
}
delegate_Test_foo_Method.prototype._getClass = delegate_Test_foo_Method__getClass;

function delegate_Test_foo_Method__getField(name) {
    return null;
}
delegate_Test_foo_Method.prototype._getField = delegate_Test_foo_Method__getField;

function delegate_Test_foo_Method__setField(name, value) {}
delegate_Test_foo_Method.prototype._setField = delegate_Test_foo_Method__setField;

// CLASS delegate_Test_rpc_Method

function delegate_Test_rpc_Method() {
    delegate_Test_rpc_Method.super_.call(this, "delegate.Message", "rpc", ["quark.String", "delegate.Message", "quark.List<quark.Object>"]);
}
exports.delegate_Test_rpc_Method = delegate_Test_rpc_Method;
_qrt.util.inherits(delegate_Test_rpc_Method, quark.reflect.Method);

function delegate_Test_rpc_Method__init_fields__() {
    quark.reflect.Method.prototype.__init_fields__.call(this);
}
delegate_Test_rpc_Method.prototype.__init_fields__ = delegate_Test_rpc_Method__init_fields__;

function delegate_Test_rpc_Method_invoke(object, args) {
    var obj = object;
    return (obj).rpc((args)[0], (args)[1], (args)[2]);
}
delegate_Test_rpc_Method.prototype.invoke = delegate_Test_rpc_Method_invoke;

function delegate_Test_rpc_Method__getClass() {
    return null;
}
delegate_Test_rpc_Method.prototype._getClass = delegate_Test_rpc_Method__getClass;

function delegate_Test_rpc_Method__getField(name) {
    return null;
}
delegate_Test_rpc_Method.prototype._getField = delegate_Test_rpc_Method__getField;

function delegate_Test_rpc_Method__setField(name, value) {}
delegate_Test_rpc_Method.prototype._setField = delegate_Test_rpc_Method__setField;

// CLASS delegate_Test_hello_Method

function delegate_Test_hello_Method() {
    delegate_Test_hello_Method.super_.call(this, "delegate.Pong", "hello", ["delegate.Ping"]);
}
exports.delegate_Test_hello_Method = delegate_Test_hello_Method;
_qrt.util.inherits(delegate_Test_hello_Method, quark.reflect.Method);

function delegate_Test_hello_Method__init_fields__() {
    quark.reflect.Method.prototype.__init_fields__.call(this);
}
delegate_Test_hello_Method.prototype.__init_fields__ = delegate_Test_hello_Method__init_fields__;

function delegate_Test_hello_Method_invoke(object, args) {
    var obj = object;
    return (obj).hello((args)[0]);
}
delegate_Test_hello_Method.prototype.invoke = delegate_Test_hello_Method_invoke;

function delegate_Test_hello_Method__getClass() {
    return null;
}
delegate_Test_hello_Method.prototype._getClass = delegate_Test_hello_Method__getClass;

function delegate_Test_hello_Method__getField(name) {
    return null;
}
delegate_Test_hello_Method.prototype._getField = delegate_Test_hello_Method__getField;

function delegate_Test_hello_Method__setField(name, value) {}
delegate_Test_hello_Method.prototype._setField = delegate_Test_hello_Method__setField;

// CLASS delegate_Test

function delegate_Test() {
    delegate_Test.super_.call(this, "delegate.Test");
    (this).name = "delegate.Test";
    (this).parameters = [];
    (this).fields = [];
    (this).methods = [new delegate_Test_bar_Method(), new delegate_Test_foo_Method(), new delegate_Test_rpc_Method(), new delegate_Test_hello_Method()];
}
exports.delegate_Test = delegate_Test;
_qrt.util.inherits(delegate_Test, quark.reflect.Class);

function delegate_Test__init_fields__() {
    quark.reflect.Class.prototype.__init_fields__.call(this);
}
delegate_Test.prototype.__init_fields__ = delegate_Test__init_fields__;
delegate_Test.singleton = new delegate_Test();
function delegate_Test_construct(args) {
    return new delegate.Test();
}
delegate_Test.prototype.construct = delegate_Test_construct;

function delegate_Test__getClass() {
    return null;
}
delegate_Test.prototype._getClass = delegate_Test__getClass;

function delegate_Test__getField(name) {
    return null;
}
delegate_Test.prototype._getField = delegate_Test__getField;

function delegate_Test__setField(name, value) {}
delegate_Test.prototype._setField = delegate_Test__setField;


// CLASS quark_List_quark_Object_

function quark_List_quark_Object_() {
    quark_List_quark_Object_.super_.call(this, "quark.List<quark.Object>");
    (this).name = "quark.List";
    (this).parameters = ["quark.Object"];
    (this).fields = [];
    (this).methods = [];
}
exports.quark_List_quark_Object_ = quark_List_quark_Object_;
_qrt.util.inherits(quark_List_quark_Object_, quark.reflect.Class);

function quark_List_quark_Object___init_fields__() {
    quark.reflect.Class.prototype.__init_fields__.call(this);
}
quark_List_quark_Object_.prototype.__init_fields__ = quark_List_quark_Object___init_fields__;
quark_List_quark_Object_.singleton = new quark_List_quark_Object_();
function quark_List_quark_Object__construct(args) {
    return new Array();
}
quark_List_quark_Object_.prototype.construct = quark_List_quark_Object__construct;

function quark_List_quark_Object___getClass() {
    return null;
}
quark_List_quark_Object_.prototype._getClass = quark_List_quark_Object___getClass;

function quark_List_quark_Object___getField(name) {
    return null;
}
quark_List_quark_Object_.prototype._getField = quark_List_quark_Object___getField;

function quark_List_quark_Object___setField(name, value) {}
quark_List_quark_Object_.prototype._setField = quark_List_quark_Object___setField;


// CLASS Root
function Root() {
    this.__init_fields__();
}
exports.Root = Root;

function Root__init_fields__() {}
Root.prototype.__init_fields__ = Root__init_fields__;
Root.delegate_Message_md = delegate_Message.singleton;
Root.delegate_Ping_md = delegate_Ping.singleton;
Root.delegate_Pong_md = delegate_Pong.singleton;
Root.delegate_Test_md = delegate_Test.singleton;
Root.quark_List_quark_Object__md = quark_List_quark_Object_.singleton;
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

var delegate = require('../delegate/index.js');
exports.delegate = delegate;

var _qrt = require("builtin/quark_runtime.js");
var testlib = require('../testlib/index.js');
exports.testlib = testlib;



function test() {
    /* import testlib; */

    var f = testlib.foo();
    _qrt.print(f);
}
exports.test = test;

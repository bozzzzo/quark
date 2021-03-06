var _qrt = require("quark/quark_runtime.js");
var pkg = require('../pkg/index.js');
exports.pkg = pkg;


exports.call_main = function () { main(process.argv.slice(1)); }
function main(args) {
    var t1 = new pkg.T1();
    (t1).foo();
    (t1).bar();
    _qrt.print("===");
    var t2 = new pkg.T2();
    (t2).foo();
    (t2).bar();
    _qrt.print("===");
    var t3 = new pkg.T3();
    (t3).foo();
    (t3).bar();
    _qrt.print("===");
    var t4 = new pkg.T4();
    (t4).foo();
    (t4).bar();
    _qrt.print("===");
    var t5 = new pkg.T5();
    (t5).foo();
    (t5).bar();
}
exports.main = main;

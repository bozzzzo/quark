var _qrt = require("quark/quark_runtime.js");

exports.call_main = function () { main(process.argv.slice(1)); }
function main(args) {
    if (true) {
        _qrt.print("Hi!");
    }
    var b = (1) > (0);
    if (b) {
        _qrt.print("Hey!");
    }
    var c = false;
    if (!(c)) {
        _qrt.print("Ho!");
    }
    var count = 0;
    while (true) {
        if ((count) > (3)) {
            break;
        }
        count = (count) + (1);
    }
    var troo = (true) && (true);
    _qrt.print((troo).toString());
    var fols = (false) || (false);
    _qrt.print((fols).toString());
    var foo = "foo";
    var bar = "bar";
    if ((_qrt.equals((foo), ("foo"))) && (_qrt.equals((bar), ("bar")))) {
        _qrt.print("foobar!!");
    }
}
exports.main = main;

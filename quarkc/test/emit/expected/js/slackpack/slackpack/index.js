var _qrt = require("quark/quark_runtime.js");
var slack = require('../slack/index.js');
exports.slack = slack;
var pkg = require('../pkg/index.js');
exports.pkg = pkg;


exports.call_main = function () { main(process.argv.slice(1)); }
function main(args) {
    var cli = new slack.Client(null, "fake-token", new pkg.Handler());
    (cli).onWSMessage(null, "{\"type\": \"hello\"}");
    (cli).onWSMessage(null, "{\"type\": \"message\", \"user\": \"uid-1\", \"channel\": \"chanel-1\"}");
}
exports.main = main;

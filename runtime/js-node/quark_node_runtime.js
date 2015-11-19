/*
 * Copyright 2015 datawire. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// Quark's Node Runtime and associated
/* jshint node: true */

(function () {
    "use strict";

    var assert = require("assert");

    var WebSocket = require("ws");

    var runtime = require("quark_runtime.js");

    // CLASS QuarkWebsocket
    function QuarkWebSocket(url, handler) {
        this.url = url;
        this.socket = new WebSocket(url);
        //this.handler = handler;
        this.isOpen = false;

        var self = this;
        handler.onWSInit(self);

        this.socket.on("open", function () {
            self.isOpen = true;
            handler.onWSConnected(self);
        });
        this.socket.on("message", function (message, flags) {
            if (flags.binary) {
                handler.onWSBinary(self, new runtime._Buffer(message));
            } else {
                handler.onWSMessage(self, message);
            }
        });
        this.socket.on("close", function (/* code, message */) {
            handler.onWSClosed(self);
            self.socket.terminate();
            handler.onWSFinal(self);
        });
        this.socket.on("error", function (/* error */) {
            handler.onWSError(self);
            self.socket.terminate();
            handler.onWSFinal(self);
        });
    }
    QuarkWebSocket.prototype.send = function (message) {
        if (this.isOpen) {
            this.socket.send(message);
            return 1;
        }
        return 0;
    };
    QuarkWebSocket.prototype.sendBinary = function(message) {
        if (this.isOpen) {
            this.socket.send(message.data, {binary:true});
            return 1;
        }
        return 0;
    };

    var http = require("http");
    var https = require("https");
    var url = require("url");

    // CLASS QuarkRequest
    function QuarkRequest(request, handler) {
        var options = url.parse(request.url);
        options.method = request.method;

        handler.onHTTPInit(request);

        var protocol = http;
        if (options.protocol === "https:") {
            protocol = https;
        }

        options.headers = JSON.parse(JSON.stringify(request.headers));  // Make a copy
        if (request.body) {
            options.headers["Content-Length"] = Buffer.byteLength(request.body);
        }

        var req = protocol.request(options);
        req.on("response", function (response) {
            var body = "";
            response.on("data", function (data) {
                body += data;
            });
            response.on("end", function () {
                handler.onHTTPResponse(request, new QuarkResponse(response.statusCode, body));
                req.abort();
                handler.onHTTPFinal(request);
            });
        });

        req.on("error", function (/* error */) {
            handler.onHTTPError(request);
            req.abort();
            handler.onHTTPFinal(request);
        });

        if (request.body) {
            req.write(request.body);
        }
        req.end();
    }

    // CLASS QuarkResponse
    function QuarkResponse(code, body) {
        this.code = code;
        this.body = body;
    }
    QuarkResponse.prototype.getCode = function () {
        return this.code;
    };
    QuarkResponse.prototype.getBody = function () {
        return this.body;
    };

    // CLASS Runtime
    function Runtime() {
        this.locked = false;
    }
    Runtime.prototype.acquire = function () {
        assert(!this.locked);
        this.locked = true;
    };
    Runtime.prototype.release = function () {
        assert(this.locked);
        this.locked = false;
    };
    Runtime.prototype.wait = function (/* timeoutInSeconds */) {
        assert(this.locked);
        assert(false);
    };
    Runtime.prototype.open = function (url, handler) {
        new QuarkWebSocket(url, handler);
    };

    Runtime.prototype.request = function (request, handler) {
        new QuarkRequest(request, handler);
    };

    Runtime.prototype.schedule = function (handler, delayInSeconds) {
        var self = this;
        setTimeout(function () { handler.onExecute(self); },
                   delayInSeconds * 1000);
    };
    Runtime.prototype.launch = function () {};

    Runtime.prototype.codec = function() { return runtime.defaultCodec(); };


    module.exports = new Runtime();

})();
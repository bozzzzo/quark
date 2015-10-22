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

import os, pytest
import wsgiref.simple_server
import threading

__all__ = "check_file assert_file maybe_xfail hello_server".split()

def check_file(path, content):
    try:
        with open(path) as fd:
            expected = fd.read()
    except IOError, e:
        expected = None
    if expected != content:
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(path + ".cmp", "wb") as fd:
            fd.write(content)
    return expected

def assert_file(path, content):
    expected = check_file(path, content)
    assert content == expected

def maybe_xfail(code):
    if "xfail" in code:
        pytest.xfail()

class hello_server(object):
    def __init__(self):
        self.server = wsgiref.simple_server.make_server("127.0.0.1", 9999, self)

    def start(self):
        def run():
            self.server.serve_forever()
        self.thread = threading.Thread(target=run)
        self.thread.start()

    def stop(self):
        self.server.shutdown()
        self.thread.join()

    def __call__(self, env, start_response):
        status = '200 OK'
        response_body = env.get('PATH_INFO', 'hello server!').lstrip('/')
        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body)))
        ]
        start_response(status, response_headers)
        return [response_body]




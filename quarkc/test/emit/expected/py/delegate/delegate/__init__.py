from quark_runtime import *

<<<<<<< HEAD:quarkc/test/emit/expected/py/delegate/delegate_lib/__init__.py
=======
import quark.reflect
import delegate_md


class Message(object):
    def _init(self):
        pass
    def __init__(self): self._init()

    def encode(self):
        return u"ENCODED"

    def _getClass(self):
        return u"delegate.Message"

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
Message.delegate_Message_ref = delegate_md.Root.delegate_Message_md
class Ping(Message):
    def _init(self):
        Message._init(self)

    def __init__(self):
        super(Ping, self).__init__();

    def _getClass(self):
        return u"delegate.Ping"

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
Ping.delegate_Ping_ref = delegate_md.Root.delegate_Ping_md
class Pong(Message):
    def _init(self):
        Message._init(self)

    def __init__(self):
        super(Pong, self).__init__();

    def toString(self):
        return u"PONG"

    def _getClass(self):
        return u"delegate.Pong"

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
Pong.delegate_Pong_ref = delegate_md.Root.delegate_Pong_md
class Test(object):
    def _init(self):
        pass
    def __init__(self): self._init()

    def bar(self, name, args, options):
        _println(args);
        return None

    def foo(self, foo, bar, baz):
        (self).bar(u"foo", _List([foo, bar, baz]), _List([]));

    def rpc(self, name, msg, options):
        _println((msg).encode());
        if ((name) == (u"hello")):
            return Pong()
        else:
            return None

    def hello(self, ping):
        return self.rpc(u"hello", ping, _List([]))

    def _getClass(self):
        return u"delegate.Test"

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
Test.delegate_Test_ref = delegate_md.Root.delegate_Test_md
Test.quark_List_quark_Object__ref = delegate_md.Root.quark_List_quark_Object__md
>>>>>>> febff07:quarkc/test/emit/expected/py/delegate/delegate/__init__.py

def main():
    _println(u"This shadows ruby builtin module 'delegate'");

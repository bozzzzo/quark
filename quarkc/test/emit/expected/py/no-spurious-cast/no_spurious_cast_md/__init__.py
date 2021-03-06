from quark_runtime import *

import quark.reflect


class no_spurious_cast_A(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(no_spurious_cast_A, self).__init__(u"no_spurious_cast.A");
        (self).name = u"no_spurious_cast.A"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([])

    def construct(self, args):
        return no_spurious_cast.A()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
no_spurious_cast_A.singleton = no_spurious_cast_A()

class no_spurious_cast_B(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(no_spurious_cast_B, self).__init__(u"no_spurious_cast.B");
        (self).name = u"no_spurious_cast.B"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([])

    def construct(self, args):
        return no_spurious_cast.B()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
no_spurious_cast_B.singleton = no_spurious_cast_B()

class no_spurious_cast_X_quark_int_(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(no_spurious_cast_X_quark_int_, self).__init__(u"no_spurious_cast.X<quark.int>");
        (self).name = u"no_spurious_cast.X"
        (self).parameters = _List([u"quark.int"])
        (self).fields = _List([])
        (self).methods = _List([])

    def construct(self, args):
        return no_spurious_cast.X()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
no_spurious_cast_X_quark_int_.singleton = no_spurious_cast_X_quark_int_()

class no_spurious_cast_Y(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(no_spurious_cast_Y, self).__init__(u"no_spurious_cast.Y");
        (self).name = u"no_spurious_cast.Y"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([])

    def construct(self, args):
        return no_spurious_cast.Y()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
no_spurious_cast_Y.singleton = no_spurious_cast_Y()

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
Root.no_spurious_cast_A_md = no_spurious_cast_A.singleton
Root.no_spurious_cast_B_md = no_spurious_cast_B.singleton
Root.no_spurious_cast_X_quark_int__md = no_spurious_cast_X_quark_int_.singleton
Root.no_spurious_cast_Y_md = no_spurious_cast_Y.singleton

import no_spurious_cast

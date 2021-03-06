from quark_runtime import *

import quark.reflect
import slack
import slack.event
import slackpack_md


class Handler(object):
    def _init(self):
        pass
    def __init__(self): self._init()

    def onSlackEvent(self, event):
        _println((event).type);
        if (((event).user) != (None)):
            _println(((event).user).user);

        if (((event).channel) != (None)):
            _println(((event).channel).channel);

    def _getClass(self):
        return u"pkg.Handler"

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

    def onHello(self, hello):
        (self).onSlackEvent(hello);

    def onSlackError(self, error):
        (self).onSlackEvent(error);

    def onMessage(self, message):
        (self).onSlackEvent(message);

Handler.pkg_Handler_ref = slackpack_md.Root.pkg_Handler_md

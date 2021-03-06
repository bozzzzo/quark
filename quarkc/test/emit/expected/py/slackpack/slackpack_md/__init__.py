from quark_runtime import *

import quark.reflect


class slack_event_SlackEvent_load_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_event_SlackEvent_load_Method, self).__init__(u"quark.void", u"load", _List([u"slack.Client", u"quark.JSONObject"]));

    def invoke(self, object, args):
        obj = object;
        (obj).load((args)[0], (args)[1]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_event_SlackEvent_dispatch_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_event_SlackEvent_dispatch_Method, self).__init__(u"quark.void", u"dispatch", _List([u"slack.SlackHandler"]));

    def invoke(self, object, args):
        obj = object;
        (obj).dispatch((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_event_SlackEvent(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_event_SlackEvent, self).__init__(u"slack.event.SlackEvent");
        (self).name = u"slack.event.SlackEvent"
        (self).parameters = _List([])
        (self).fields = _List([quark.reflect.Field(u"quark.String", u"type"), quark.reflect.Field(u"slack.User", u"user"), quark.reflect.Field(u"slack.Channel", u"channel"), quark.reflect.Field(u"quark.String", u"timestamp")])
        (self).methods = _List([slack_event_SlackEvent_load_Method(), slack_event_SlackEvent_dispatch_Method()])

    def construct(self, args):
        return slack.event.SlackEvent()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_event_SlackEvent.singleton = slack_event_SlackEvent()

class slack_event_SlackError_load_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_event_SlackError_load_Method, self).__init__(u"quark.void", u"load", _List([u"slack.Client", u"quark.JSONObject"]));

    def invoke(self, object, args):
        obj = object;
        (obj).load((args)[0], (args)[1]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_event_SlackError_dispatch_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_event_SlackError_dispatch_Method, self).__init__(u"quark.void", u"dispatch", _List([u"slack.SlackHandler"]));

    def invoke(self, object, args):
        obj = object;
        (obj).dispatch((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_event_SlackError(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_event_SlackError, self).__init__(u"slack.event.SlackError");
        (self).name = u"slack.event.SlackError"
        (self).parameters = _List([])
        (self).fields = _List([quark.reflect.Field(u"quark.String", u"type"), quark.reflect.Field(u"slack.User", u"user"), quark.reflect.Field(u"slack.Channel", u"channel"), quark.reflect.Field(u"quark.String", u"timestamp"), quark.reflect.Field(u"quark.int", u"code"), quark.reflect.Field(u"quark.String", u"text")])
        (self).methods = _List([slack_event_SlackError_load_Method(), slack_event_SlackError_dispatch_Method()])

    def construct(self, args):
        return slack.event.SlackError()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_event_SlackError.singleton = slack_event_SlackError()

class slack_event_Hello_dispatch_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_event_Hello_dispatch_Method, self).__init__(u"quark.void", u"dispatch", _List([u"slack.SlackHandler"]));

    def invoke(self, object, args):
        obj = object;
        (obj).dispatch((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_event_Hello_load_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_event_Hello_load_Method, self).__init__(u"quark.void", u"load", _List([u"slack.Client", u"quark.JSONObject"]));

    def invoke(self, object, args):
        obj = object;
        (obj).load((args)[0], (args)[1]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_event_Hello(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_event_Hello, self).__init__(u"slack.event.Hello");
        (self).name = u"slack.event.Hello"
        (self).parameters = _List([])
        (self).fields = _List([quark.reflect.Field(u"quark.String", u"type"), quark.reflect.Field(u"slack.User", u"user"), quark.reflect.Field(u"slack.Channel", u"channel"), quark.reflect.Field(u"quark.String", u"timestamp")])
        (self).methods = _List([slack_event_Hello_dispatch_Method(), slack_event_Hello_load_Method()])

    def construct(self, args):
        return slack.event.Hello()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_event_Hello.singleton = slack_event_Hello()

class slack_event_Message_load_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_event_Message_load_Method, self).__init__(u"quark.void", u"load", _List([u"slack.Client", u"quark.JSONObject"]));

    def invoke(self, object, args):
        obj = object;
        (obj).load((args)[0], (args)[1]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_event_Message_dispatch_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_event_Message_dispatch_Method, self).__init__(u"quark.void", u"dispatch", _List([u"slack.SlackHandler"]));

    def invoke(self, object, args):
        obj = object;
        (obj).dispatch((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_event_Message(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_event_Message, self).__init__(u"slack.event.Message");
        (self).name = u"slack.event.Message"
        (self).parameters = _List([])
        (self).fields = _List([quark.reflect.Field(u"quark.String", u"type"), quark.reflect.Field(u"slack.User", u"user"), quark.reflect.Field(u"slack.Channel", u"channel"), quark.reflect.Field(u"quark.String", u"timestamp"), quark.reflect.Field(u"quark.String", u"subtype"), quark.reflect.Field(u"quark.bool", u"hidden"), quark.reflect.Field(u"quark.String", u"text"), quark.reflect.Field(u"slack.event.Edited", u"edited")])
        (self).methods = _List([slack_event_Message_load_Method(), slack_event_Message_dispatch_Method()])

    def construct(self, args):
        return slack.event.Message()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_event_Message.singleton = slack_event_Message()

class slack_event_Edited(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_event_Edited, self).__init__(u"slack.event.Edited");
        (self).name = u"slack.event.Edited"
        (self).parameters = _List([])
        (self).fields = _List([quark.reflect.Field(u"slack.User", u"user"), quark.reflect.Field(u"quark.String", u"timestamp")])
        (self).methods = _List([])

    def construct(self, args):
        return slack.event.Edited()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_event_Edited.singleton = slack_event_Edited()

class slack_SlackHandler_onSlackEvent_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_SlackHandler_onSlackEvent_Method, self).__init__(u"quark.void", u"onSlackEvent", _List([u"slack.event.SlackEvent"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onSlackEvent((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_SlackHandler_onHello_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_SlackHandler_onHello_Method, self).__init__(u"quark.void", u"onHello", _List([u"slack.event.Hello"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onHello((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_SlackHandler_onSlackError_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_SlackHandler_onSlackError_Method, self).__init__(u"quark.void", u"onSlackError", _List([u"slack.event.SlackError"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onSlackError((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_SlackHandler_onMessage_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_SlackHandler_onMessage_Method, self).__init__(u"quark.void", u"onMessage", _List([u"slack.event.Message"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onMessage((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_SlackHandler(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_SlackHandler, self).__init__(u"slack.SlackHandler");
        (self).name = u"slack.SlackHandler"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([slack_SlackHandler_onSlackEvent_Method(), slack_SlackHandler_onHello_Method(), slack_SlackHandler_onSlackError_Method(), slack_SlackHandler_onMessage_Method()])

    def construct(self, args):
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_SlackHandler.singleton = slack_SlackHandler()

class slack_User(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_User, self).__init__(u"slack.User");
        (self).name = u"slack.User"
        (self).parameters = _List([])
        (self).fields = _List([quark.reflect.Field(u"slack.Client", u"client"), quark.reflect.Field(u"quark.String", u"user")])
        (self).methods = _List([])

    def construct(self, args):
        return slack.User((args)[0], (args)[1])

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_User.singleton = slack_User()

class slack_Channel_send_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Channel_send_Method, self).__init__(u"quark.void", u"send", _List([u"quark.String"]));

    def invoke(self, object, args):
        obj = object;
        (obj).send((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Channel(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_Channel, self).__init__(u"slack.Channel");
        (self).name = u"slack.Channel"
        (self).parameters = _List([])
        (self).fields = _List([quark.reflect.Field(u"slack.Client", u"client"), quark.reflect.Field(u"quark.String", u"channel")])
        (self).methods = _List([slack_Channel_send_Method()])

    def construct(self, args):
        return slack.Channel((args)[0], (args)[1])

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_Channel.singleton = slack_Channel()

class slack_Client_connect_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_connect_Method, self).__init__(u"quark.void", u"connect", _List([]));

    def invoke(self, object, args):
        obj = object;
        (obj).connect();
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_request_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_request_Method, self).__init__(u"quark.void", u"request", _List([u"quark.String", u"quark.Map<quark.String,quark.Object>", u"quark.HTTPHandler"]));

    def invoke(self, object, args):
        obj = object;
        (obj).request((args)[0], (args)[1], (args)[2]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_ws_connect_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_ws_connect_Method, self).__init__(u"quark.void", u"ws_connect", _List([u"quark.String"]));

    def invoke(self, object, args):
        obj = object;
        (obj).ws_connect((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_ws_send_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_ws_send_Method, self).__init__(u"quark.void", u"ws_send", _List([u"quark.String"]));

    def invoke(self, object, args):
        obj = object;
        (obj).ws_send((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onWSConnected_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onWSConnected_Method, self).__init__(u"quark.void", u"onWSConnected", _List([u"quark.WebSocket"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onWSConnected((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onWSClose_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onWSClose_Method, self).__init__(u"quark.void", u"onWSClose", _List([u"quark.WebSocket"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onWSClose((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onWSError_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onWSError_Method, self).__init__(u"quark.void", u"onWSError", _List([u"quark.WebSocket"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onWSError((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_construct_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_construct_Method, self).__init__(u"slack.event.SlackEvent", u"construct", _List([u"quark.String"]));

    def invoke(self, object, args):
        obj = object;
        return (obj).construct((args)[0])

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onWSMessage_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onWSMessage_Method, self).__init__(u"quark.void", u"onWSMessage", _List([u"quark.WebSocket", u"quark.String"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onWSMessage((args)[0], (args)[1]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onHTTPResponse_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onHTTPResponse_Method, self).__init__(u"quark.void", u"onHTTPResponse", _List([u"quark.HTTPRequest", u"quark.HTTPResponse"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onHTTPResponse((args)[0], (args)[1]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onWSInit_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onWSInit_Method, self).__init__(u"quark.void", u"onWSInit", _List([u"quark.WebSocket"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onWSInit((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onWSBinary_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onWSBinary_Method, self).__init__(u"quark.void", u"onWSBinary", _List([u"quark.WebSocket", u"quark.Buffer"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onWSBinary((args)[0], (args)[1]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onWSClosed_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onWSClosed_Method, self).__init__(u"quark.void", u"onWSClosed", _List([u"quark.WebSocket"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onWSClosed((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onWSFinal_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onWSFinal_Method, self).__init__(u"quark.void", u"onWSFinal", _List([u"quark.WebSocket"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onWSFinal((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onHTTPInit_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onHTTPInit_Method, self).__init__(u"quark.void", u"onHTTPInit", _List([u"quark.HTTPRequest"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onHTTPInit((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onHTTPError_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onHTTPError_Method, self).__init__(u"quark.void", u"onHTTPError", _List([u"quark.HTTPRequest", u"quark.String"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onHTTPError((args)[0], (args)[1]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client_onHTTPFinal_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(slack_Client_onHTTPFinal_Method, self).__init__(u"quark.void", u"onHTTPFinal", _List([u"quark.HTTPRequest"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onHTTPFinal((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class slack_Client(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(slack_Client, self).__init__(u"slack.Client");
        (self).name = u"slack.Client"
        (self).parameters = _List([])
        (self).fields = _List([quark.reflect.Field(u"quark.Runtime", u"runtime"), quark.reflect.Field(u"quark.String", u"token"), quark.reflect.Field(u"slack.SlackHandler", u"handler"), quark.reflect.Field(u"quark.int", u"event_id"), quark.reflect.Field(u"quark.WebSocket", u"socket")])
        (self).methods = _List([slack_Client_connect_Method(), slack_Client_request_Method(), slack_Client_ws_connect_Method(), slack_Client_ws_send_Method(), slack_Client_onWSConnected_Method(), slack_Client_onWSClose_Method(), slack_Client_onWSError_Method(), slack_Client_construct_Method(), slack_Client_onWSMessage_Method(), slack_Client_onHTTPResponse_Method(), slack_Client_onWSInit_Method(), slack_Client_onWSBinary_Method(), slack_Client_onWSClosed_Method(), slack_Client_onWSFinal_Method(), slack_Client_onHTTPInit_Method(), slack_Client_onHTTPError_Method(), slack_Client_onHTTPFinal_Method()])

    def construct(self, args):
        return slack.Client((args)[0], (args)[1], (args)[2])

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
slack_Client.singleton = slack_Client()

class pkg_Handler_onSlackEvent_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_Handler_onSlackEvent_Method, self).__init__(u"quark.void", u"onSlackEvent", _List([u"slack.event.SlackEvent"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onSlackEvent((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_Handler_onHello_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_Handler_onHello_Method, self).__init__(u"quark.void", u"onHello", _List([u"slack.event.Hello"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onHello((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_Handler_onSlackError_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_Handler_onSlackError_Method, self).__init__(u"quark.void", u"onSlackError", _List([u"slack.event.SlackError"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onSlackError((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_Handler_onMessage_Method(quark.reflect.Method):
    def _init(self):
        quark.reflect.Method._init(self)

    def __init__(self):
        super(pkg_Handler_onMessage_Method, self).__init__(u"quark.void", u"onMessage", _List([u"slack.event.Message"]));

    def invoke(self, object, args):
        obj = object;
        (obj).onMessage((args)[0]);
        return None

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass

class pkg_Handler(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(pkg_Handler, self).__init__(u"pkg.Handler");
        (self).name = u"pkg.Handler"
        (self).parameters = _List([])
        (self).fields = _List([])
        (self).methods = _List([pkg_Handler_onSlackEvent_Method(), pkg_Handler_onHello_Method(), pkg_Handler_onSlackError_Method(), pkg_Handler_onMessage_Method()])

    def construct(self, args):
        return pkg.Handler()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
pkg_Handler.singleton = pkg_Handler()

class quark_Map_quark_String_quark_Object_(quark.reflect.Class):
    def _init(self):
        quark.reflect.Class._init(self)

    def __init__(self):
        super(quark_Map_quark_String_quark_Object_, self).__init__(u"quark.Map<quark.String,quark.Object>");
        (self).name = u"quark.Map"
        (self).parameters = _List([u"quark.String", u"quark.Object"])
        (self).fields = _List([])
        (self).methods = _List([])

    def construct(self, args):
        return _Map()

    def _getClass(self):
        return None

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
quark_Map_quark_String_quark_Object_.singleton = quark_Map_quark_String_quark_Object_()

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
Root.slack_event_SlackEvent_md = slack_event_SlackEvent.singleton
Root.slack_event_SlackError_md = slack_event_SlackError.singleton
Root.slack_event_Hello_md = slack_event_Hello.singleton
Root.slack_event_Message_md = slack_event_Message.singleton
Root.slack_event_Edited_md = slack_event_Edited.singleton
Root.slack_SlackHandler_md = slack_SlackHandler.singleton
Root.slack_User_md = slack_User.singleton
Root.slack_Channel_md = slack_Channel.singleton
Root.slack_Client_md = slack_Client.singleton
Root.pkg_Handler_md = pkg_Handler.singleton
Root.quark_Map_quark_String_quark_Object__md = quark_Map_quark_String_quark_Object_.singleton

import slack.event
import slack
import quark
import pkg

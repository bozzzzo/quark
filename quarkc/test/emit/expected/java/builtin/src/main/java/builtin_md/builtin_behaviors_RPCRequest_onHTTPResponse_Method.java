package builtin_md;

public class builtin_behaviors_RPCRequest_onHTTPResponse_Method extends builtin.reflect.Method implements io.datawire.quark.runtime.QObject {
    public builtin_behaviors_RPCRequest_onHTTPResponse_Method() {
        super("builtin.void", "onHTTPResponse", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"builtin.HTTPRequest", "builtin.HTTPResponse"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        builtin.behaviors.RPCRequest obj = (builtin.behaviors.RPCRequest) (object);
        (obj).onHTTPResponse((io.datawire.quark.runtime.HTTPRequest) ((args).get(0)), (io.datawire.quark.runtime.HTTPResponse) ((args).get(1)));
        return null;
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}

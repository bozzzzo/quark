package quark_md;

public class quark_behaviors_RPCRequest_onHTTPFinal_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public quark_behaviors_RPCRequest_onHTTPFinal_Method() {
        super("quark.void", "onHTTPFinal", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"quark.HTTPRequest"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        quark.behaviors.RPCRequest obj = (quark.behaviors.RPCRequest) (object);
        (obj).onHTTPFinal((quark.HTTPRequest) ((args).get(0)));
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

package builtin.behaviors;

public class RPC implements io.datawire.quark.runtime.QObject {
    public static builtin.reflect.Class builtin_behaviors_RPC_ref = builtin_md.Root.builtin_behaviors_RPC_md;
    public builtin.Service service;
    public builtin.reflect.Class returned;
    public Long timeout;
    public String name;
    public RPC(builtin.Service service, String name, java.util.ArrayList<Object> options) {
        Long timeout = (service).getTimeout();
        if (((options).size()) > (0)) {
            java.util.HashMap<String,Object> map = (java.util.HashMap<String,Object>) ((options).get(0));
            Integer override = (Integer) ((map).get("timeout"));
            if (!((override)==(null) || ((override) != null && (override).equals(null)))) {
                timeout = new Long(override);
            }
        }
        (this).returned = ((builtin.reflect.Class.get(io.datawire.quark.runtime.Builtins._getClass(service))).getMethod(name)).getType();
        (this).timeout = timeout;
        (this).name = name;
        (this).service = service;
    }
    public builtin.concurrent.Future call(Object message) {
        io.datawire.quark.runtime.HTTPRequest request = new io.datawire.quark.runtime.ClientHTTPRequest(((this).service).getURL());
        io.datawire.quark.runtime.JSONObject json = builtin.Functions.toJSON(message);
        io.datawire.quark.runtime.JSONObject envelope = new io.datawire.quark.runtime.JSONObject();
        (envelope).setObjectItem(("$method"), ((new io.datawire.quark.runtime.JSONObject()).setString((this).name)));
        (envelope).setObjectItem(("$context"), ((new io.datawire.quark.runtime.JSONObject()).setString("TBD")));
        (envelope).setObjectItem(("rpc"), (json));
        (request).setBody((envelope).toString());
        (request).setMethod("POST");
        RPCRequest rpc = new RPCRequest(message, this);
        builtin.concurrent.Future result = (rpc).call(request);
        builtin.concurrent.FutureWait.waitFor(result, new Long(1000));
        return result;
    }
    public String _getClass() {
        return "builtin.behaviors.RPC";
    }
    public Object _getField(String name) {
        if ((name)==("service") || ((name) != null && (name).equals("service"))) {
            return (this).service;
        }
        if ((name)==("returned") || ((name) != null && (name).equals("returned"))) {
            return (this).returned;
        }
        if ((name)==("timeout") || ((name) != null && (name).equals("timeout"))) {
            return (this).timeout;
        }
        if ((name)==("name") || ((name) != null && (name).equals("name"))) {
            return (this).name;
        }
        return null;
    }
    public void _setField(String name, Object value) {
        if ((name)==("service") || ((name) != null && (name).equals("service"))) {
            (this).service = (builtin.Service) (value);
        }
        if ((name)==("returned") || ((name) != null && (name).equals("returned"))) {
            (this).returned = (builtin.reflect.Class) (value);
        }
        if ((name)==("timeout") || ((name) != null && (name).equals("timeout"))) {
            (this).timeout = (Long) (value);
        }
        if ((name)==("name") || ((name) != null && (name).equals("name"))) {
            (this).name = (String) (value);
        }
    }
}
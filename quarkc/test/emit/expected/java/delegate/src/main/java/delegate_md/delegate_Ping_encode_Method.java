package delegate_md;

public class delegate_Ping_encode_Method extends builtin.reflect.Method implements io.datawire.quark.runtime.QObject {
    public delegate_Ping_encode_Method() {
        super("builtin.String", "encode", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        delegate.Ping obj = (delegate.Ping) (object);
        return (obj).encode();
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}

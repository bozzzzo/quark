package quark_md;

public class quark_concurrent_Context_swap_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public quark_concurrent_Context_swap_Method() {
        super("quark.void", "swap", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"quark.concurrent.Context"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        quark.concurrent.Context obj = (quark.concurrent.Context) (object);
        quark.concurrent.Context.swap((quark.concurrent.Context) ((args).get(0)));
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

package quark_md;

public class quark_concurrent_FutureWait_waitFor_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public quark_concurrent_FutureWait_waitFor_Method() {
        super("quark.concurrent.Future", "waitFor", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"quark.concurrent.Future", "quark.float"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        quark.concurrent.FutureWait obj = (quark.concurrent.FutureWait) (object);
        return quark.concurrent.FutureWait.waitFor((quark.concurrent.Future) ((args).get(0)), (Double) ((args).get(1)));
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}

package quark_md;

public class quark_logging_Config_setAppender_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public quark_logging_Config_setAppender_Method() {
        super("quark.logging.Config", "setAppender", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"quark.logging.Appender"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        quark.logging.Config obj = (quark.logging.Config) (object);
        return (obj).setAppender((quark.logging.Appender) ((args).get(0)));
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}

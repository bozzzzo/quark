package string_methods_md;

public class string_methods_test_endsWith_that_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public string_methods_test_endsWith_that_Method() {
        super("string_methods.test_endsWith", "that", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"quark.String"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        string_methods.test_endsWith obj = (string_methods.test_endsWith) (object);
        return (obj).that((String) ((args).get(0)));
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}

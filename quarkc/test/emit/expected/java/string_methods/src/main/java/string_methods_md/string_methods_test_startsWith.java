package string_methods_md;

public class string_methods_test_startsWith extends quark.reflect.Class implements io.datawire.quark.runtime.QObject {
    public static quark.reflect.Class singleton = new string_methods_test_startsWith();
    public string_methods_test_startsWith() {
        super("string_methods.test_startsWith");
        (this).name = "string_methods.test_startsWith";
        (this).parameters = new java.util.ArrayList(java.util.Arrays.asList(new Object[]{}));
        (this).fields = new java.util.ArrayList(java.util.Arrays.asList(new Object[]{new quark.reflect.Field("quark.String", "what"), new quark.reflect.Field("quark.String", "_that")}));
        (this).methods = new java.util.ArrayList(java.util.Arrays.asList(new Object[]{new string_methods_test_startsWith_that_Method(), new string_methods_test_startsWith_does_Method(), new string_methods_test_startsWith_check_Method()}));
    }
    public Object construct(java.util.ArrayList<Object> args) {
        return new string_methods.test_startsWith((String) ((args).get(0)));
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}

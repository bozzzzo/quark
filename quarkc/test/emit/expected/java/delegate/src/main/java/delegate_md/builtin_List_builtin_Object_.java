package delegate_md;

public class builtin_List_builtin_Object_ extends builtin.reflect.Class implements io.datawire.quark.runtime.QObject {
    public static builtin.reflect.Class singleton = new builtin_List_builtin_Object_();
    public builtin_List_builtin_Object_() {
        super("builtin.List<builtin.Object>");
        (this).name = "builtin.List";
        (this).parameters = new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"builtin.Object"}));
        (this).fields = new java.util.ArrayList(java.util.Arrays.asList(new Object[]{}));
        (this).methods = new java.util.ArrayList(java.util.Arrays.asList(new Object[]{}));
    }
    public Object construct(java.util.ArrayList<Object> args) {
        return new java.util.ArrayList<Object>();
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}

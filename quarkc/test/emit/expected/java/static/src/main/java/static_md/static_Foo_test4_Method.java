package static_md;

public class static_Foo_test4_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public static_Foo_test4_Method() {
        super("quark.void", "test4", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        static_.Foo obj = (static_.Foo) (object);
        (obj).test4();
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

package super_md;

public class super_A_greet_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public super_A_greet_Method() {
        super("quark.void", "greet", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        super_.A obj = (super_.A) (object);
        (obj).greet();
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

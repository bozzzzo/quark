package use_class_before_def_md;

public class pkg_Bar_go_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public pkg_Bar_go_Method() {
        super("quark.void", "go", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        pkg.Bar obj = (pkg.Bar) (object);
        (obj).go();
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

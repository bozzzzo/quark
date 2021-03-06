package string_methods;

public class test_join extends string_test implements io.datawire.quark.runtime.QObject {
    public static quark.reflect.Class string_methods_test_join_ref = string_methods_md.Root.string_methods_test_join_md;
    public static quark.reflect.Class quark_List_quark_String__ref = string_methods_md.Root.quark_List_quark_String__md;
    public String what;
    public java.util.ArrayList<String> parts;
    public String strparts;
    public String sep;
    public test_join(String what) {
        super();
        (this).what = what;
    }
    public test_join that() {
        (this).parts = new java.util.ArrayList<String>();
        (this).strparts = "";
        (this).sep = "";
        return this;
    }
    public test_join a(String part) {
        ((this).parts).add(part);
        (this).strparts = (((((this).strparts) + ((this).sep)) + ("'")) + (part)) + ("'");
        (this).sep = ", ";
        return this;
    }
    public test_join does(String expected) {
        (this).check(io.datawire.quark.runtime.Builtins.join(((this).what), ((this).parts)), expected, (((("'") + ((this).what)) + ("'.join([")) + ((this).strparts)) + ("])"), "'");
        return this;
    }
    public String _getClass() {
        return "string_methods.test_join";
    }
    public Object _getField(String name) {
        if ((name)==("what") || ((Object)(name) != null && ((Object) (name)).equals("what"))) {
            return (this).what;
        }
        if ((name)==("parts") || ((Object)(name) != null && ((Object) (name)).equals("parts"))) {
            return (this).parts;
        }
        if ((name)==("strparts") || ((Object)(name) != null && ((Object) (name)).equals("strparts"))) {
            return (this).strparts;
        }
        if ((name)==("sep") || ((Object)(name) != null && ((Object) (name)).equals("sep"))) {
            return (this).sep;
        }
        return null;
    }
    public void _setField(String name, Object value) {
        if ((name)==("what") || ((Object)(name) != null && ((Object) (name)).equals("what"))) {
            (this).what = (String) (value);
        }
        if ((name)==("parts") || ((Object)(name) != null && ((Object) (name)).equals("parts"))) {
            (this).parts = (java.util.ArrayList<String>) (value);
        }
        if ((name)==("strparts") || ((Object)(name) != null && ((Object) (name)).equals("strparts"))) {
            (this).strparts = (String) (value);
        }
        if ((name)==("sep") || ((Object)(name) != null && ((Object) (name)).equals("sep"))) {
            (this).sep = (String) (value);
        }
    }
}

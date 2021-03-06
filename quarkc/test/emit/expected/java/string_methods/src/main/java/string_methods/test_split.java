package string_methods;

public class test_split extends string_test implements io.datawire.quark.runtime.QObject {
    public static quark.reflect.Class string_methods_test_split_ref = string_methods_md.Root.string_methods_test_split_md;
    public String what;
    public String sep;
    public String altsep;
    public test_split(String sep, String altsep) {
        super();
        (this).sep = sep;
        (this).altsep = altsep;
    }
    public test_split that(String what) {
        (this).what = what;
        return this;
    }
    public test_split does(String expected) {
        java.util.ArrayList<String> parts = new java.util.ArrayList<String>(java.util.Arrays.asList(((this).what).split(java.util.regex.Pattern.quote((this).sep), -1)));
        String actual = io.datawire.quark.runtime.Builtins.join(((this).altsep), (parts));
        (this).check(actual, expected, (((((("'") + ((this).altsep)) + ("'.join('")) + ((this).what)) + ("'.split('")) + ((this).sep)) + ("'))"), "'");
        return this;
    }
    public String _getClass() {
        return "string_methods.test_split";
    }
    public Object _getField(String name) {
        if ((name)==("what") || ((Object)(name) != null && ((Object) (name)).equals("what"))) {
            return (this).what;
        }
        if ((name)==("sep") || ((Object)(name) != null && ((Object) (name)).equals("sep"))) {
            return (this).sep;
        }
        if ((name)==("altsep") || ((Object)(name) != null && ((Object) (name)).equals("altsep"))) {
            return (this).altsep;
        }
        return null;
    }
    public void _setField(String name, Object value) {
        if ((name)==("what") || ((Object)(name) != null && ((Object) (name)).equals("what"))) {
            (this).what = (String) (value);
        }
        if ((name)==("sep") || ((Object)(name) != null && ((Object) (name)).equals("sep"))) {
            (this).sep = (String) (value);
        }
        if ((name)==("altsep") || ((Object)(name) != null && ((Object) (name)).equals("altsep"))) {
            (this).altsep = (String) (value);
        }
    }
}

package builtin.concurrent;

/**
 * The logical stack for async stuff.
 */
public class Context implements io.datawire.quark.runtime.QObject {
    public static Context _global = new Context(null);
    public static io.datawire.quark.runtime.TLS<Context> _current = new io.datawire.quark.runtime.TLS(new TLSContextInitializer());
    public static builtin.reflect.Class builtin_concurrent_Context_ref = builtin_md.Root.builtin_concurrent_Context_md;
    public Context _parent;
    public io.datawire.quark.runtime.Runtime _runtime;
    public Collector collector;
    public Context(Context parent) {
        (this)._parent = parent;
        if ((parent)==(null) || ((parent) != null && (parent).equals(null))) {
            (this)._runtime = io.datawire.quark.runtime.Runtime.Factory.create();
            (this).collector = new Collector();
        } else {
            (this)._runtime = (parent)._runtime;
            (this).collector = (parent).collector;
        }
    }
    public static Context current() {
        return (Context._current).getValue();
    }
    public static Context global() {
        return Context._global;
    }
    public static io.datawire.quark.runtime.Runtime runtime() {
        return (Context.current())._runtime;
    }
    public static void swap(Context c) {
        (Context._current).setValue(c);
    }
    public String _getClass() {
        return "builtin.concurrent.Context";
    }
    public Object _getField(String name) {
        if ((name)==("_global") || ((name) != null && (name).equals("_global"))) {
            return Context._global;
        }
        if ((name)==("_current") || ((name) != null && (name).equals("_current"))) {
            return Context._current;
        }
        if ((name)==("_parent") || ((name) != null && (name).equals("_parent"))) {
            return (this)._parent;
        }
        if ((name)==("_runtime") || ((name) != null && (name).equals("_runtime"))) {
            return (this)._runtime;
        }
        if ((name)==("collector") || ((name) != null && (name).equals("collector"))) {
            return (this).collector;
        }
        return null;
    }
    public void _setField(String name, Object value) {
        if ((name)==("_global") || ((name) != null && (name).equals("_global"))) {
            Context._global = (Context) (value);
        }
        if ((name)==("_current") || ((name) != null && (name).equals("_current"))) {
            Context._current = (io.datawire.quark.runtime.TLS<Context>) (value);
        }
        if ((name)==("_parent") || ((name) != null && (name).equals("_parent"))) {
            (this)._parent = (Context) (value);
        }
        if ((name)==("_runtime") || ((name) != null && (name).equals("_runtime"))) {
            (this)._runtime = (io.datawire.quark.runtime.Runtime) (value);
        }
        if ((name)==("collector") || ((name) != null && (name).equals("collector"))) {
            (this).collector = (Collector) (value);
        }
    }
}

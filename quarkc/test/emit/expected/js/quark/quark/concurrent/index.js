var _qrt = require("quark/quark_runtime.js");
var quark = require('../../quark/index.js');
exports.quark = quark;
var quark_md = require('../../quark_md/index.js');
exports.quark_md = quark_md;
var quark = require('../../quark/index.js');
exports.quark = quark;
var quark = require('../../quark/index.js');
exports.quark = quark;



// CLASS Event
/**
 * The contract between event implementations and Collector
 */
function Event() {
    this.__init_fields__();
}
exports.Event = Event;

function Event__init_fields__() {}
Event.prototype.__init_fields__ = Event__init_fields__;
Event.quark_concurrent_Event_ref = quark_md.Root.quark_concurrent_Event_md;
function Event_getContext() { /* interface */ }
Event.prototype.getContext = Event_getContext;

function Event_fireEvent() { /* interface */ }
Event.prototype.fireEvent = Event_fireEvent;

// CLASS FutureListener
/**
 * event handler for a future completion
 */
function FutureListener() {
    this.__init_fields__();
}
exports.FutureListener = FutureListener;

function FutureListener__init_fields__() {}
FutureListener.prototype.__init_fields__ = FutureListener__init_fields__;
FutureListener.quark_concurrent_FutureListener_ref = quark_md.Root.quark_concurrent_FutureListener_md;
function FutureListener_onFuture(future) {}
FutureListener.prototype.onFuture = FutureListener_onFuture;

// CLASS FutureCompletion
/**
 * internal class that binds a listener to a future
 */

function FutureCompletion(future, listener) {
    this.__init_fields__();
    (this).future = future;
    (this).listener = listener;
}
exports.FutureCompletion = FutureCompletion;

function FutureCompletion__init_fields__() {
    this.future = null;
    this.listener = null;
}
FutureCompletion.prototype.__init_fields__ = FutureCompletion__init_fields__;
FutureCompletion.quark_concurrent_FutureCompletion_ref = quark_md.Root.quark_concurrent_FutureCompletion_md;
function FutureCompletion_getContext() {
    return (this).future;
}
FutureCompletion.prototype.getContext = FutureCompletion_getContext;

function FutureCompletion_fireEvent() {
    ((this).listener).onFuture((this).future);
}
FutureCompletion.prototype.fireEvent = FutureCompletion_fireEvent;

function FutureCompletion__getClass() {
    return "quark.concurrent.FutureCompletion";
}
FutureCompletion.prototype._getClass = FutureCompletion__getClass;

function FutureCompletion__getField(name) {
    if (_qrt.equals((name), ("future"))) {
        return (this).future;
    }
    if (_qrt.equals((name), ("listener"))) {
        return (this).listener;
    }
    return null;
}
FutureCompletion.prototype._getField = FutureCompletion__getField;

function FutureCompletion__setField(name, value) {
    if (_qrt.equals((name), ("future"))) {
        (this).future = value;
    }
    if (_qrt.equals((name), ("listener"))) {
        (this).listener = value;
    }
}
FutureCompletion.prototype._setField = FutureCompletion__setField;

// CLASS EventContext
/**
 * Captures the current context, base class for all event source implementations
 */

function EventContext() {
    this.__init_fields__();
    (this)._context = Context.current();
}
exports.EventContext = EventContext;

function EventContext__init_fields__() {
    this._context = null;
}
EventContext.prototype.__init_fields__ = EventContext__init_fields__;
EventContext.quark_concurrent_EventContext_ref = quark_md.Root.quark_concurrent_EventContext_md;
function EventContext_getContext() {
    return (this)._context;
}
EventContext.prototype.getContext = EventContext_getContext;

function EventContext__getClass() {
    return "quark.concurrent.EventContext";
}
EventContext.prototype._getClass = EventContext__getClass;

function EventContext__getField(name) {
    if (_qrt.equals((name), ("_context"))) {
        return (this)._context;
    }
    return null;
}
EventContext.prototype._getField = EventContext__getField;

function EventContext__setField(name, value) {
    if (_qrt.equals((name), ("_context"))) {
        (this)._context = value;
    }
}
EventContext.prototype._setField = EventContext__setField;

// CLASS Future
/**
 * The base class for value objects
 */

function Future() {
    Future.super_.call(this);
    (this)._finished = false;
    (this)._callbacks = null;
    (this)._lock = new _qrt.Lock();
}
exports.Future = Future;
_qrt.util.inherits(Future, EventContext);

function Future__init_fields__() {
    EventContext.prototype.__init_fields__.call(this);
    this._finished = null;
    this._error = null;
    this._callbacks = null;
    this._lock = null;
}
Future.prototype.__init_fields__ = Future__init_fields__;
Future.quark_List_quark_concurrent_FutureCompletion__ref = quark_md.Root.quark_List_quark_concurrent_FutureCompletion__md;
Future.quark_concurrent_Future_ref = quark_md.Root.quark_concurrent_Future_md;
function Future_onFinished(callback) {
    ((this)._lock).acquire();
    if ((this)._finished) {
        (((this)._context).collector).put(new FutureCompletion(this, callback));
    } else {
        if (_qrt.equals(((this)._callbacks), (null))) {
            (this)._callbacks = [];
        }
        ((this)._callbacks).push(new FutureCompletion(this, callback));
    }
    ((this)._lock).release();
}
Future.prototype.onFinished = Future_onFinished;

function Future_finish(error) {
    var callbacks = null;
    ((this)._lock).acquire();
    if (!((this)._finished)) {
        (this)._finished = true;
        (this)._error = error;
        callbacks = (this)._callbacks;
        (this)._callbacks = null;
    }
    ((this)._lock).release();
    if ((callbacks) !== (null)) {
        var i = 0;
        while ((i) < ((callbacks).length)) {
            (((this)._context).collector).put((callbacks)[i]);
            i = (i) + (1);
        }
    }
}
Future.prototype.finish = Future_finish;

function Future_isFinished() {
    ((this)._lock).acquire();
    var finished = (this)._finished;
    ((this)._lock).release();
    return finished;
}
Future.prototype.isFinished = Future_isFinished;

function Future_getError() {
    ((this)._lock).acquire();
    var error = (this)._error;
    ((this)._lock).release();
    return error;
}
Future.prototype.getError = Future_getError;

function Future_await(timeout) {
    (new FutureWait()).wait(this, timeout);
}
Future.prototype.await = Future_await;

function Future__getClass() {
    return "quark.concurrent.Future";
}
Future.prototype._getClass = Future__getClass;

function Future__getField(name) {
    if (_qrt.equals((name), ("_context"))) {
        return (this)._context;
    }
    if (_qrt.equals((name), ("_finished"))) {
        return (this)._finished;
    }
    if (_qrt.equals((name), ("_error"))) {
        return (this)._error;
    }
    if (_qrt.equals((name), ("_callbacks"))) {
        return (this)._callbacks;
    }
    if (_qrt.equals((name), ("_lock"))) {
        return (this)._lock;
    }
    return null;
}
Future.prototype._getField = Future__getField;

function Future__setField(name, value) {
    if (_qrt.equals((name), ("_context"))) {
        (this)._context = value;
    }
    if (_qrt.equals((name), ("_finished"))) {
        (this)._finished = value;
    }
    if (_qrt.equals((name), ("_error"))) {
        (this)._error = value;
    }
    if (_qrt.equals((name), ("_callbacks"))) {
        (this)._callbacks = value;
    }
    if (_qrt.equals((name), ("_lock"))) {
        (this)._lock = value;
    }
}
Future.prototype._setField = Future__setField;

// CLASS FutureWait
/**
 * Synchronization point for a Future.)
 */

function FutureWait() {
    this.__init_fields__();
    (this)._lock = new _qrt.Condition();
    (this)._future = null;
}
exports.FutureWait = FutureWait;

function FutureWait__init_fields__() {
    this._lock = null;
    this._future = null;
}
FutureWait.prototype.__init_fields__ = FutureWait__init_fields__;
FutureWait.quark_concurrent_FutureWait_ref = quark_md.Root.quark_concurrent_FutureWait_md;
function FutureWait_wait(future, timeout) {
    if ((future).isFinished()) {
        return;
    }
    (this)._future = future;
    ((this)._future).onFinished(this);
    var rounded = Math.round((1000.0) * (timeout));
    var deadline = (Date.now()) + (rounded);
    while (!(((this)._future).isFinished())) {
        var remaining = (deadline) - (Date.now());
        if ((rounded) !== (0)) {
            if ((remaining) <= ((0))) {
                break;
            }
        } else {
            remaining = (3141);
        }
        ((this)._lock).acquire();
        ((this)._lock).waitWakeup(remaining);
        ((this)._lock).release();
    }
    (this)._future = null;
}
FutureWait.prototype.wait = FutureWait_wait;

function FutureWait_onFuture(future) {
    ((this)._lock).acquire();
    ((this)._lock).wakeup();
    ((this)._lock).release();
}
FutureWait.prototype.onFuture = FutureWait_onFuture;

function FutureWait_waitFor(future, timeout) {
    if (false) {
        var w = new FutureWait();
        (w).wait(future, timeout);
        if (!((future).isFinished())) {}
    }
    return future;
}
FutureWait.waitFor = FutureWait_waitFor;

function FutureWait__getClass() {
    return "quark.concurrent.FutureWait";
}
FutureWait.prototype._getClass = FutureWait__getClass;

function FutureWait__getField(name) {
    if (_qrt.equals((name), ("_lock"))) {
        return (this)._lock;
    }
    if (_qrt.equals((name), ("_future"))) {
        return (this)._future;
    }
    return null;
}
FutureWait.prototype._getField = FutureWait__getField;

function FutureWait__setField(name, value) {
    if (_qrt.equals((name), ("_lock"))) {
        (this)._lock = value;
    }
    if (_qrt.equals((name), ("_future"))) {
        (this)._future = value;
    }
}
FutureWait.prototype._setField = FutureWait__setField;

// CLASS Queue
/**
 * A simple FIFO
 */

function Queue() {
    this.__init_fields__();
    (this).items = new Array();
    (this).head = 0;
    (this).tail = 0;
}
exports.Queue = Queue;

function Queue__init_fields__() {
    this.items = null;
    this.head = null;
    this.tail = null;
}
Queue.prototype.__init_fields__ = Queue__init_fields__;

function Queue_put(item) {
    if (((this).tail) < (((this).items).length)) {
        ((this).items)[(this).tail] = (item);
    } else {
        ((this).items).push(item);
    }
    (this).tail = ((this).tail) + (1);
}
Queue.prototype.put = Queue_put;

function Queue_get() {
    var item = null;
    if (((this).head) < ((this).tail)) {
        item = ((this).items)[(this).head];
        (this).head = ((this).head) + (1);
    } else {
        if (((this).head) > (0)) {
            (this).head = 0;
            (this).tail = 0;
        }
    }
    return item;
}
Queue.prototype.get = Queue_get;

function Queue_size() {
    return ((this).tail) - ((this).head);
}
Queue.prototype.size = Queue_size;

function Queue__getClass() {
    return "quark.concurrent.Queue<quark.Object>";
}
Queue.prototype._getClass = Queue__getClass;

function Queue__getField(name) {
    if (_qrt.equals((name), ("items"))) {
        return (this).items;
    }
    if (_qrt.equals((name), ("head"))) {
        return (this).head;
    }
    if (_qrt.equals((name), ("tail"))) {
        return (this).tail;
    }
    return null;
}
Queue.prototype._getField = Queue__getField;

function Queue__setField(name, value) {
    if (_qrt.equals((name), ("items"))) {
        (this).items = value;
    }
    if (_qrt.equals((name), ("head"))) {
        (this).head = value;
    }
    if (_qrt.equals((name), ("tail"))) {
        (this).tail = value;
    }
}
Queue.prototype._setField = Queue__setField;

// CLASS CollectorExecutor
/**
 * Fire events one by one with no locks held
 */

function CollectorExecutor(collector) {
    this.__init_fields__();
    (this).events = new Queue();
    (this).collector = collector;
}
exports.CollectorExecutor = CollectorExecutor;

function CollectorExecutor__init_fields__() {
    this.events = null;
    this.collector = null;
}
CollectorExecutor.prototype.__init_fields__ = CollectorExecutor__init_fields__;
CollectorExecutor.quark_concurrent_Queue_quark_concurrent_Event__ref = quark_md.Root.quark_concurrent_Queue_quark_concurrent_Event__md;
CollectorExecutor.quark_concurrent_CollectorExecutor_ref = quark_md.Root.quark_concurrent_CollectorExecutor_md;
function CollectorExecutor__start() {
    (this).events = ((this).collector)._swap((this).events);
    if ((((this).events).size()) > (0)) {
        (Context.runtime()).schedule(this, 0.0);
    }
}
CollectorExecutor.prototype._start = CollectorExecutor__start;

function CollectorExecutor_onExecute(runtime) {
    var next = ((this).events).get();
    var old = Context.current();
    while ((next) !== (null)) {
        Context.swap(((next).getContext()).getContext());
        (next).fireEvent();
        next = ((this).events).get();
    }
    Context.swap(old);
    ((this).collector)._poll();
}
CollectorExecutor.prototype.onExecute = CollectorExecutor_onExecute;

function CollectorExecutor__getClass() {
    return "quark.concurrent.CollectorExecutor";
}
CollectorExecutor.prototype._getClass = CollectorExecutor__getClass;

function CollectorExecutor__getField(name) {
    if (_qrt.equals((name), ("events"))) {
        return (this).events;
    }
    if (_qrt.equals((name), ("collector"))) {
        return (this).collector;
    }
    return null;
}
CollectorExecutor.prototype._getField = CollectorExecutor__getField;

function CollectorExecutor__setField(name, value) {
    if (_qrt.equals((name), ("events"))) {
        (this).events = value;
    }
    if (_qrt.equals((name), ("collector"))) {
        (this).collector = value;
    }
}
CollectorExecutor.prototype._setField = CollectorExecutor__setField;

// CLASS Collector
/**
 * An active queue of events. Each event will fire sequentially, one by one. Multiple instances of Collector are not serialized with eachother and may run in parallel.
 */

function Collector() {
    this.__init_fields__();
    (this).lock = new _qrt.Lock();
    (this).pending = new Queue();
    (this).executor = new CollectorExecutor(this);
    (this).idle = true;
}
exports.Collector = Collector;

function Collector__init_fields__() {
    this.lock = null;
    this.pending = null;
    this.executor = null;
    this.idle = null;
}
Collector.prototype.__init_fields__ = Collector__init_fields__;
Collector.quark_concurrent_Collector_ref = quark_md.Root.quark_concurrent_Collector_md;
function Collector_put(event) {
    ((this).lock).acquire();
    ((this).pending).put(event);
    if ((this).idle) {
        ((this).executor)._start();
    }
    ((this).lock).release();
}
Collector.prototype.put = Collector_put;

function Collector__swap(drained) {
    var pending = (this).pending;
    (this).idle = _qrt.equals(((pending).size()), (0));
    (this).pending = drained;
    return pending;
}
Collector.prototype._swap = Collector__swap;

function Collector__poll() {
    ((this).lock).acquire();
    ((this).executor)._start();
    ((this).lock).release();
}
Collector.prototype._poll = Collector__poll;

function Collector__getClass() {
    return "quark.concurrent.Collector";
}
Collector.prototype._getClass = Collector__getClass;

function Collector__getField(name) {
    if (_qrt.equals((name), ("lock"))) {
        return (this).lock;
    }
    if (_qrt.equals((name), ("pending"))) {
        return (this).pending;
    }
    if (_qrt.equals((name), ("executor"))) {
        return (this).executor;
    }
    if (_qrt.equals((name), ("idle"))) {
        return (this).idle;
    }
    return null;
}
Collector.prototype._getField = Collector__getField;

function Collector__setField(name, value) {
    if (_qrt.equals((name), ("lock"))) {
        (this).lock = value;
    }
    if (_qrt.equals((name), ("pending"))) {
        (this).pending = value;
    }
    if (_qrt.equals((name), ("executor"))) {
        (this).executor = value;
    }
    if (_qrt.equals((name), ("idle"))) {
        (this).idle = value;
    }
}
Collector.prototype._setField = Collector__setField;

// CLASS TimeoutListener
/**
 * Timeout expiry handler
 */
function TimeoutListener() {
    this.__init_fields__();
}
exports.TimeoutListener = TimeoutListener;

function TimeoutListener__init_fields__() {}
TimeoutListener.prototype.__init_fields__ = TimeoutListener__init_fields__;
TimeoutListener.quark_concurrent_TimeoutListener_ref = quark_md.Root.quark_concurrent_TimeoutListener_md;
function TimeoutListener_onTimeout(timeout) { /* interface */ }
TimeoutListener.prototype.onTimeout = TimeoutListener_onTimeout;

// CLASS TimeoutExpiry
/**
 * Timeout expiry event
 */

function TimeoutExpiry(timeout, listener) {
    this.__init_fields__();
    (this).timeout = timeout;
    (this).listener = listener;
}
exports.TimeoutExpiry = TimeoutExpiry;

function TimeoutExpiry__init_fields__() {
    this.timeout = null;
    this.listener = null;
}
TimeoutExpiry.prototype.__init_fields__ = TimeoutExpiry__init_fields__;
TimeoutExpiry.quark_concurrent_TimeoutExpiry_ref = quark_md.Root.quark_concurrent_TimeoutExpiry_md;
function TimeoutExpiry_getContext() {
    return (this).timeout;
}
TimeoutExpiry.prototype.getContext = TimeoutExpiry_getContext;

function TimeoutExpiry_fireEvent() {
    ((this).listener).onTimeout((this).timeout);
}
TimeoutExpiry.prototype.fireEvent = TimeoutExpiry_fireEvent;

function TimeoutExpiry__getClass() {
    return "quark.concurrent.TimeoutExpiry";
}
TimeoutExpiry.prototype._getClass = TimeoutExpiry__getClass;

function TimeoutExpiry__getField(name) {
    if (_qrt.equals((name), ("timeout"))) {
        return (this).timeout;
    }
    if (_qrt.equals((name), ("listener"))) {
        return (this).listener;
    }
    return null;
}
TimeoutExpiry.prototype._getField = TimeoutExpiry__getField;

function TimeoutExpiry__setField(name, value) {
    if (_qrt.equals((name), ("timeout"))) {
        (this).timeout = value;
    }
    if (_qrt.equals((name), ("listener"))) {
        (this).listener = value;
    }
}
TimeoutExpiry.prototype._setField = TimeoutExpiry__setField;

// CLASS Timeout
/**
 * Timeout
 */

function Timeout(timeout) {
    Timeout.super_.call(this);
    (this).timeout = timeout;
    (this).listener = null;
    (this).lock = new _qrt.Lock();
}
exports.Timeout = Timeout;
_qrt.util.inherits(Timeout, EventContext);

function Timeout__init_fields__() {
    EventContext.prototype.__init_fields__.call(this);
    this.timeout = null;
    this.lock = null;
    this.listener = null;
}
Timeout.prototype.__init_fields__ = Timeout__init_fields__;
Timeout.quark_concurrent_Timeout_ref = quark_md.Root.quark_concurrent_Timeout_md;
function Timeout_start(listener) {
    (this).listener = listener;
    var delay = (this).timeout;
    (Context.runtime()).schedule(this, delay);
}
Timeout.prototype.start = Timeout_start;

function Timeout_cancel() {
    ((this).lock).acquire();
    (this).listener = null;
    ((this).lock).release();
}
Timeout.prototype.cancel = Timeout_cancel;

function Timeout_onExecute(runtime) {
    ((this).lock).acquire();
    if (((this).listener) !== (null)) {
        (((this)._context).collector).put(new TimeoutExpiry(this, (this).listener));
        (this).listener = null;
    }
    ((this).lock).release();
}
Timeout.prototype.onExecute = Timeout_onExecute;

function Timeout__getClass() {
    return "quark.concurrent.Timeout";
}
Timeout.prototype._getClass = Timeout__getClass;

function Timeout__getField(name) {
    if (_qrt.equals((name), ("_context"))) {
        return (this)._context;
    }
    if (_qrt.equals((name), ("timeout"))) {
        return (this).timeout;
    }
    if (_qrt.equals((name), ("lock"))) {
        return (this).lock;
    }
    if (_qrt.equals((name), ("listener"))) {
        return (this).listener;
    }
    return null;
}
Timeout.prototype._getField = Timeout__getField;

function Timeout__setField(name, value) {
    if (_qrt.equals((name), ("_context"))) {
        (this)._context = value;
    }
    if (_qrt.equals((name), ("timeout"))) {
        (this).timeout = value;
    }
    if (_qrt.equals((name), ("lock"))) {
        (this).lock = value;
    }
    if (_qrt.equals((name), ("listener"))) {
        (this).listener = value;
    }
}
Timeout.prototype._setField = Timeout__setField;

// CLASS TLSContextInitializer
/**
 * internal
 */
function TLSContextInitializer() {
    this.__init_fields__();
}
exports.TLSContextInitializer = TLSContextInitializer;

function TLSContextInitializer__init_fields__() {}
TLSContextInitializer.prototype.__init_fields__ = TLSContextInitializer__init_fields__;
TLSContextInitializer.quark_concurrent_TLSContextInitializer_ref = quark_md.Root.quark_concurrent_TLSContextInitializer_md;
function TLSContextInitializer_getValue() {
    return new Context(Context.global());
}
TLSContextInitializer.prototype.getValue = TLSContextInitializer_getValue;

function TLSContextInitializer__getClass() {
    return "quark.concurrent.TLSContextInitializer";
}
TLSContextInitializer.prototype._getClass = TLSContextInitializer__getClass;

function TLSContextInitializer__getField(name) {
    return null;
}
TLSContextInitializer.prototype._getField = TLSContextInitializer__getField;

function TLSContextInitializer__setField(name, value) {}
TLSContextInitializer.prototype._setField = TLSContextInitializer__setField;

// CLASS Context
/**
 * The logical stack for async stuff.
 */

function Context(parent) {
    this.__init_fields__();
    (this)._parent = parent;
    if (_qrt.equals((parent), (null))) {
        (this)._runtime = (quark.spi.RuntimeFactory.factory).makeRuntime();
        (this).collector = new Collector();
    } else {
        (this)._runtime = (parent)._runtime;
        (this).collector = (parent).collector;
    }
}
exports.Context = Context;

function Context__init_fields__() {
    this._parent = null;
    this._runtime = null;
    this.collector = null;
}
Context.prototype.__init_fields__ = Context__init_fields__;
Context._global = null;
Context._current = new _qrt.TLS(new TLSContextInitializer());
Context.quark_concurrent_Context_ref = quark_md.Root.quark_concurrent_Context_md;
function Context_current() {
    return (Context._current).getValue();
}
Context.current = Context_current;

function Context_global() {
    if (_qrt.equals((Context._global), (null))) {
        Context._global = new Context(null);
    }
    return Context._global;
}
Context.global = Context_global;

function Context_runtime() {
    return (Context.current())._runtime;
}
Context.runtime = Context_runtime;

function Context_swap(c) {
    (Context._current).setValue(c);
}
Context.swap = Context_swap;

function Context__getClass() {
    return "quark.concurrent.Context";
}
Context.prototype._getClass = Context__getClass;

function Context__getField(name) {
    if (_qrt.equals((name), ("_global"))) {
        return Context._global;
    }
    if (_qrt.equals((name), ("_current"))) {
        return Context._current;
    }
    if (_qrt.equals((name), ("_parent"))) {
        return (this)._parent;
    }
    if (_qrt.equals((name), ("_runtime"))) {
        return (this)._runtime;
    }
    if (_qrt.equals((name), ("collector"))) {
        return (this).collector;
    }
    return null;
}
Context.prototype._getField = Context__getField;

function Context__setField(name, value) {
    if (_qrt.equals((name), ("_global"))) {
        Context._global = value;
    }
    if (_qrt.equals((name), ("_current"))) {
        Context._current = value;
    }
    if (_qrt.equals((name), ("_parent"))) {
        (this)._parent = value;
    }
    if (_qrt.equals((name), ("_runtime"))) {
        (this)._runtime = value;
    }
    if (_qrt.equals((name), ("collector"))) {
        (this).collector = value;
    }
}
Context.prototype._setField = Context__setField;

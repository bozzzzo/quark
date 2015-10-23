
class Later extends Async<String> {
    void callback(String result) {
        print("later: " + result);
    }
    void errback(String failure) {
        print("later failure: " + failure);
    }
}

class Requestbin extends Async<String> {
    int done;
    Requestbin() {
        self.done = 42;
    }
    void callback(String result) {
        done = done + 13;
        print("requestbin: " + result + " done=" + done.toString());
    }
    void errback(String failure) {
        done = done + 1;
        print("requestbin failure: " + failure);
    }
}

void main() {
    Async<String> l = new Later();
    l.callback("expected");
    l.errback("expected");
    Requestbin r = new Requestbin();
    url_get_async("http://127.0.0.1:9998/yay!", r);
    url_get_async("http://127.0.0.1:9999/yay!", r);
}

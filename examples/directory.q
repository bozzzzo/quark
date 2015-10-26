package directory {

    class Directory { // implements WebHandler, Task

	Runtime runtime;
	WebSocket socket;

	bool initialized;
	Map<String,Entry> entries;
	float timeout = 60.0;
	List<AsyncLookup> deferred = [];

        Directory(Runtime runtime, String url) {
	    self.runtime = runtime;
	    self.runtime.acquire(); // would be nice to have a with statement or something
	    self.socket = self.runtime.open(url);
	    self.socket.setHandler(self);
	    JSONObject jobj = new JSONObject(); // or maybe just new Map<String,Object> if that can work
	    jobj["tether-info"] = "...";
	    self.socket.send(jobj.toString()); // might need to be toJSON() or something like that

	    self.runtime.schedule(self, 3.0); // heartbeat interval

	    self.runtime.release();
        }

	void onExecute(Runtime runtime) {
	    self.socket.send("{heartbeat-info...}");
	}

	void onMessage(WebSocket socket, String message) {
	    JSONObject jobj = JSONObject.parse(message);
	    String op = jobj["op"];
	    if (op == "entry") {
		Entry entry = new Entry();
		entry.service = jobj["service"];
		entry.endpoints = jobj["endpoints"];
		entries[entry.service] = entry;
	    } else {
		if (op == "initialized") {
		    self.initialized = true;
		    self.fireDeferred();
		}
	    }
	}

        Entry lookup(String name) {
	    Entry result = null;
	    self.runtime.aquire();
	    while (!self.initialized) {
		self.runtime.wait(self.timeout);
	    }
	    result = entries[name];
	    self.runtime.release();
	    return result;
        }

	Future<Entry> lookupAsync(String name) {
	    AsyncLookup result;
	    self.directory.runtime.acquire();
	    result = new AsyncLookup(self, name);
	    if (self.initialized) {
		self.runtime.schedule(result);
	    } else {
		self.deferred.append(result);
	    }
	    self.directory.runtime.release();
	    return result;
	}

    }

    class AsyncLookup { // implements Task, Future<Entry>
	Directory directory;
	String name;
	Entry result;

	AsyncLookup(Directory directory, String name) {
	    self.name = name;
	    self.directory = directory;
	    self.result = null;
	}

	void onExecute(Runtime runtime) {
	    self.result = self.directory.entries[self.name];
	    // fire completion on future here???
	}
    }

    class Entry {
	String service;
	List<String> endpoints;
    }

}
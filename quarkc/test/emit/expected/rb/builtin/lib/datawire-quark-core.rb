module DatawireQuarkCore
  require 'net/http'
  require 'uri'
  require 'json'
  require 'concurrent'
  require 'celluloid/current'
  require 'reel'
  require 'logging'
  require 'event_emitter'

  class Extern
    def self.getters(*names)
      names.each do |name|
        define_method('get' + to_camel_case(name)) do
          instance_variable_get("@#{name}")
        end
      end
    end

    def self.setters(*names)
      names.each do |name|
        define_method('set' + to_camel_case(name)) do |value|
          instance_variable_set("@#{name}", value)

          nil
        end
      end
    end

  private

    def self.to_camel_case(string)
      string.to_s.split('_').collect(&:capitalize).join
    end
  end

  module Static
    Unassigned = Class.new

        def unlazy_statics
          names = _lazy_statics
          # puts "unlazying #{self.name} fields #{names}"
          names.each do |name|
            self.send(name)
          end
        end
        def _lazy_statics
          lazy = :@_lazy_statics
          if not self.instance_variable_defined? lazy
            # puts "Bootstrap #{self.name}"
            l = self.instance_variable_set(lazy, {:__owner__ => self.name})
          else
            l = self.instance_variable_get(lazy)
          end
          if not l.has_key? self.name
            o = l[:__owner__]
            # puts "Adding slot for #{self.name} to lazy of #{o}"
            l[self.name] = []
          end
          l[self.name]
        end
        def static(pairs)
          pairs.each do |name, default|
            _lazy_statics << name
            self.instance_variable_set("@#{name}", Unassigned)

            define_singleton_method(name) do
              value = self.instance_variable_get("@#{name}")

              if value == Unassigned
                value = default.call
                self.instance_variable_set("@#{name}", value)
              end

              value
            end

            define_singleton_method("#{name}=") do |value|
              self.instance_variable_set("@#{name}", value)
            end

            define_method(name) do
              self.class.send(name)
            end

            define_method("#{name}=") do |value|
              self.class.send("#{name}=", value)
            end
          end
        end
  end

  def self.print(message)
    Kernel.print message == nil ? 'null' : message, "\n"
  end

  def self.urlencode(hash)
    URI.encode_www_form hash
  end

  def self.split(string, separator)
    return ['', ''] if string == separator
    result = string.split(separator)
    result = result + [''] if string.end_with? separator

    result
  end

  def self.now
    (Time.now.to_f * 1000).round
  end

  def self._getClass obj
    clz = __getClass obj
    # puts "runtime _getClass for #{obj} is #{clz}"
    clz
  end
  def self.__getClass obj
    return nil if obj.is_a? NilClass
    return "builtin.String" if obj.is_a? String
    return "builtin.int" if obj.is_a? Fixnum
    return "builtin.float" if obj.is_a? Float
    return "builtin.List<builtin.Object>" if obj.is_a? Array
    return "builtin.Map<builtin.Object,builtin.Object>" if obj.is_a? Hash
    return obj._getClass
  end

  class QuarkObject < ::BasicObject
    ### XXX: make sure to keep methods defined here in sync with list compiler's quarkc.ruby.SUBS
    def nil?
      false
    end

    def to_s
      ::Object.instance_method(:to_s).bind(self).call.gsub("::MODULE_",".").gsub("::CLASS_",".")
    end

    private
    def method_missing(name, *args, &block)
      super unless [:method, :inspect, :is_a?].find_index name
      ::Object.instance_method(name).bind(self).call(*args, &block)
    end
  end

  class List < Array
    def to_s
      '[' + map(&:to_s).join(', ') + ']'
    end
  end

  class JSONObject
    attr_accessor :value

    def initialize(value=nil)
      @value = value
    end

    def self.parse(json)
      new JSON.parse("[#{json}]")[0]
    end

    def ==(other)
      not other.nil? and value == other.value
    end

    def toString
      value.to_json
    end

    def size
      isList || isObject ? value.size : 1
    end

    def getType
      case @value
        when Hash
          'object'
        when Array
          'list'
        when String
          'string'
        when Numeric
          'number'
        when true, false
          'bool'
        when nil
          'null'
        else
          raise RuntimeError, "Unknown JSONObject type #{@value.inspect}"
      end
    end

    def set(value)
      @value = value

      self
    end

    # Object

    def isObject
      value.is_a? Hash
    end

    def setObject
      @value = {}

      self
    end

    def getObjectItem(key)
      return undefined unless isObject and value.key? key

      self.class.new value[key]
    end

    def setObjectItem(key, item)
      setObject unless isObject
      value[key] = item.value

      self
    end

    def keys
      return undefined unless isObject

      List.new value.keys
    end

    # List

    def isList
      value.is_a? Array
    end

    def setList
      @value = List.new

      self
    end

    def getListItem(index)
      return undefined unless isList and (0...size).include? index

      self.class.new value[index]
    end

    def setListItem(index, item)
      setList unless isList
      value[index] = item.value

      self
    end

    # String

    def isString
      value.is_a? String
    end

    def getString
      return nil unless isString

      value
    end

    alias_method :setString, :set

    # Number

    def isNumber
      value.is_a? Numeric
    end

    def getNumber
      return nil unless isNumber

      value
    end

    alias_method :setNumber, :set

    # Bool

    def getBool
      return nil unless isBool

      value
    end

    def isBool
      [true, false].include? value
    end

    alias_method :setBool, :set

    # Null

    def isNull
      value == nil
    end

    def setNull
      @value = nil

      self
    end

    # Undefined

    UNDEFINED = Class.new

    def isUndefined
      value == undefined
    end

    def isDefined
      not isUndefined
    end

    def undefined
      self.class.new UNDEFINED
    end
  end

  module HTTP
    class Base < Extern
      def setHeader(key, value)
        @headers[key.downcase] = value

        nil
      end

      def getHeader(key)
        @headers[key.downcase]
      end

      def getHeaders
        @headers.keys
      end
    end

    class Request < Base
      getters :body, :method, :url
      setters :body, :method

      def initialize(url)
        @url = url
        @method = 'GET'
        @body = nil
        @headers = {}
      end
    end

    class Response < Base
      getters :code, :body
      setters :code, :body

      def initialize
        @code = 500
        @body = ''
        @headers = {}
        @responded = false
      end
    end
  end

  class Sources
    def initialize()
      @sources = Concurrent::Map.new
      @seq = Concurrent::AtomicFixnum.new
    end

    def add (topic)
      key = "%s-%s" % [ @seq.increment, topic ]
      @sources.put_if_absent(key, Time.new)
      key
    end

    def remove (key)
      @sources.delete(key)
    end

    def empty?
      @sources.empty?
    end

    def explain
      @sources.each_key { |k| puts "Waiting for %s from %s" % [k, @sources[k]]}
    end
  end

  class QuarkLayout < ::Logging::Layout
    def format( event )
      obj = format_obj(event.data)
      sprintf("%s: %s\n", ::Logging::LNAMES[event.level].downcase, obj)
    end
  end
  class Logger
    extend Forwardable
    @@init = false
    def initialize(topic)
      check_init if not @@init
      @log = Logging.logger[topic.gsub(".","::")]
    end

    def check_init
      @@init = true
      r = Logging.logger.root
      if r.appenders.empty?
        r.appenders = Logging.appenders.stdout
        # Logging.logger["quark"].warn "Logging initialized by quark runtime."
      else
        # Logging.logger["quark"].debug "Logging already initialized."
      end
      # Logging.show_configuration
    end

    if Logging.level_num(:trace).nil?
      def_delegator :@log, :debug, :trace
    else
      def_delegator :@log, :trace, :trace
    end
    def_delegators :@log, :debug, :info, :warn, :error
  end


  class Eventor
    def initialize()
      @executor = Concurrent::SingleThreadExecutor.new
      @timers = Concurrent::TimerSet.new(:executor => @executor)
      @sources = Sources.new
      at_exit { wait_for_sources }
      @log = Logger.new "quark.runtime"
    end

    def add(source)
      @sources.add source
    end

    def event(final:nil, &block)
      @executor.post { execute(final, block) }
    end

    def execute(final, block)
      begin
        block.call()
      rescue => ex
        puts "aieee", ex, ex.backtrace
        @log.error ex
      ensure
        @sources.remove final if final
      end
    end

    def schedule(delay, &block)
      @timers.post(delay, &block)
    end

    def wait_for_sources
      last = Time.new - 10
      delta = 1
      while not @sources.empty?
        now = Time.new
        if now - last > delta
          @sources.explain
          last = now
          if delta < 60
            delta = delta * 1.41
          end
        end
        sleep 0.1
      end
    end

  end

  class Runtime
    def initialize()
      @events = Eventor.new
      @log = Logger.new "quark.runtime"
    end
    def schedule(task, delay)
      src = @events.add "timer"
      @events.schedule(delay) { @events.event(final:src) { task.onExecute self } }
    end
    def request(request, handler)
      src = @events.add "http request"
      t = Thread.new do
        begin
          url = request.getUrl
          @events.event { handler.onHTTPInit url }
          headers = {}
          request.getHeaders.each { |k| headers[k] = request.getHeader k }
          uri = URI(url)
          req = Net::HTTPGenericRequest.new(request.getMethod.upcase, 1, 1, uri, headers)
          req.body = request.getBody
          res = Net::HTTP.start(uri.host, uri.port) do | http |
            http.request(req)
          end
          response = HTTP::Response.new
          response.setCode(res.code.to_i)
          response.setBody(res.body)
          @events.event { handler.onHTTPResponse request, response }
        rescue Exception => e
          @log.warn "EXCEPTION: #{e.inspect}"
          @log.warn "MESSAGE: #{e.message}"
          @events.event { handler.onHTTPError request, e.message }
        ensure
          @events.event(final:src) { handler.onHTTPFinal request }
        end
      end
    end

    def serveHTTP(url, servlet)
      src = @events.add "http servlet"
      uri = URI(url)
      # TODO multiple servlets per server
      # TODO check scheme
      # TODO error handling
      @events.event { servlet.onServletInit(url, self) }
      server = MyServer.new(uri.host, uri.port) do |request|
        @events.event { servlet.onHTTPRequest(request, request.rs) }
      end
    end

    def respond(request, response)
      if request.rs == response
        request.fut.set response
      else
        request.fail!
      end
    end

    def open(url, handler)
      begin
      src = @events.add "ws client"
      client = WebsocketClient.new(url)
      sock = WebsocketAdapter.new(client)
      events = @events
      events.event { handler.onWSInit(sock) }
      client.on_client(:open) do |wsevt|
        puts "open"
        events.event { handler.onWSConnected(sock) }
      end
      client.on_client(:message) do |wsevt|
        puts "message"
        case wsevt.data
        when Array then
          buffer = Buffer.new(wsevt.data.pack("C*"))
          events.event { handler.onWSBinary(sock, buffer) }
        when String then
          events.event { handler.onWSMessage(sock, wsevt.data) }
        end
      end
      client.on_client(:close) do |wsevt|
        puts "close"
        events.event { handler.onWSClosed(sock) }
        events.event(final:src) { handler.onWSFinal(sock) }
      end
      client.on_client(:error) do |wsevt|
        puts self
        puts "error"
        events.event { handler.onWSError(sock, wsevt.reason) }
      end
      client.issues.on(:start_failed) do |err|
        events.event { handler.onWSError(sock, err.to_s) }
        events.event(final:src) { handler.onWSFinal(sock) }
      end
      Thread.new { client.run }
      rescue ::Exception => err
        puts "AIEEE", err, err.backtrace
      end
    end

    def fail(message)
      @log.fatal message
      exit! 1
    end

    def logger(topic)
      return Logger.new topic
    end

    def codec
      return Codec.new
    end
  end

  class WebsocketAdapter
    def initialize(client)
      @client = client
    end

    def send (message)
      @client.text message
    end

    def sendBinary (message)
      @client.binary message.data
    end

    def close
      @client.close
    end
  end

  class WebscketIssues
    include EventEmitter
  end
  class WebsocketClient
    extend Forwardable
    def initialize(url)
      @url = url
      @client = ::WebSocket::Driver.client(self)
      @issues = WebscketIssues.new
    end
    attr_reader :url


    def issues
      @issues
    end

    def run
      begin
        uri = URI(url)
        port = uri.port || (uri.scheme == "ws" ? 80 : 443)
        @socket = Celluloid::IO::TCPSocket.new(uri.host, port)
        @client.start
      rescue ::Exception => err
        @issues.emit(:start_failed, err)
      else
        loop do
          begin
            @client.parse(@socket.readpartial(1024))
          rescue EOFError
            break
          end
        end
      end
    end

    def_delegators :@client, :text, :binary, :ping, :close, :protocol
    def_delegator :@client, :on, :on_client

    def write(buffer)
      @socket.write buffer
    end

  end

  class IncomingRequest < HTTP::Request
    attr_accessor :rs
    attr_accessor :fut

    private

    def fail
      @rs.setCode(500)
      @rs.setBody("Servlet failed to pair up request and response")
      @fut.set(@rs)
    end
  end

  class MyServer < Reel::Server::HTTP
    def initialize(host = "127.0.0.1", port = 3000, &cb)
      super(host, port, &method(:on_connection))
      @cb = cb
    end

    def on_connection(connection)
      connection.each_request do |request|
        if request.websocket?
          handle_websocket(request.websocket)
        else
          handle_request(request)
        end
      end
    end

    def handle_request(request)
      rq = IncomingRequest.new(request.url)
      rq.setBody(request.body)
      request.headers.each {|key, value| rq.setHeader(key, value)}
      rq.setMethod(request.method)
      rq.rs = HTTP::Response.new
      rq.fut = Concurrent::IVar.new
      @cb.call(rq)
      rs = rq.fut.value
      headers = {}
      rs.getHeaders.each { |k| headers[k] = rs.getHeader k }
      response = Reel::Response::new(rs.getCode, headers, rs.getBody)
      request.respond response
    end

    def handle_websocket(sock)
      sock << "Hello everyone out there in WebSocket land!"
      sock.close
    end
  end


  HTTPRequest = HTTP::Request

  class Servlet
    def onServletInit(url, rt)
    end
    def onServletError(url, error)
    end
    def onServletEnd(url)
    end
  end
  class HTTPServlet < Servlet
    def onHTTPRequest(request, response)
    end
  end

  def self.url_get(url)
    Net::HTTP.get(URI(url))
  end

  def self.default_codec
    Codec.new
  end

  class Mutex
  end

  class Lock < Mutex
    def initialize
      @lock = ::Thread::Mutex.new
    end

    def acquire
      if @lock.owned?
        fail "Illegal re-acquisition of a quark lock"
      end
      @lock.lock
    end

    def release
      if !@lock.owned?
        fail "Illegal release of a not-acquired quark lock"
      end
       @lock.unlock
    end

    private

    def fail(reason)
      @log.fatal reason
      exit! 1  # XXX: we should go via Quark runtime, but need to develop a method to query it, Context is not yet exposed to the native code...
    end
  end

  class Condition < Lock
    def initialize
      super
      @condition = ::Thread::ConditionVariable.new
    end
    def waitWakeup(timeout)
      if !@lock.owned?
        fail "Illegal waitWakeup of a not-acquired quark Condition"
      end
      @condition.wait(@lock, timeout)
    end

    def wakeup
      if !@lock.owned?
        fail "Illegal wakeup of a not-acquired quark Condition"
      end
      @condition.signal
    end
  end

  class TLS
    UNINITIALIZED = []
    private_constant :UNINITIALIZED
    def initialize(initializer)
      @initializer = initializer
      @var = Concurrent::ThreadLocalVar.new UNINITIALIZED
    end

    def getValue
      value = @var.value
      if UNINITIALIZED.equal?(value)
        @var.value = value = @initializer.getValue
      end
      value
    end

    def setValue(value)
      @var.value = value
    end
  end

  class Codec
    ZERO = "\0".encode Encoding::ASCII_8BIT
    def buffer(size)
      Buffer.new ZERO * size
    end

    def toHexdump(buffer, index, size, spaceScale)
      hex = buffer.data[index...index+size].unpack("H*")[0]
      (0...hex.size).each_slice(2**(spaceScale+1)).map {|i|
        hex[i[0]..i[-1]]
      }.join " "
    end

    def toBase64(buffer, index, size)
      Base64.encode64(buffer.data[index...index+size]).strip
    end

    def fromHexdump(value)
      value = value.split(" ").join
      if value[0...2].downcase == "0x"
        value[0...2] = ""
      end
      Buffer.new ((0...value.length).each_slice(2).map { |i|
        value[i[0]..i[1]].to_i(16)
      }.pack("C*"))
    end

    def fromBase64(value)
      Buffer.new Base64.decode64 value
    end
  end

  class Buffer
    BIN = Encoding::ASCII_8BIT
    UTF8 = Encoding::UTF_8
    module BE
      SHORT = "s>"
      INT   = "l>"
      LONG  = "q>"
      FLOAT = "G"
    end
    module LE
      SHORT = "s<"
      INT   = "l<"
      LONG  = "q<"
      FLOAT = "E"
    end
    attr_reader :data
    def initialize(data)
      @data = data.dup.force_encoding BIN
      @ord = BE
    end
    def capacity
      @data.length
    end
    def putStringUTF8(index, value)
      value = value.dup.force_encoding BIN
      len = value.length
      @data[index...index+len] = value
      len
    end
    def getStringUTF8(index, length)
      @data[index...index+length].force_encoding UTF8
    end
    def getByte(index)
      @data[index].bytes[0]
    end
    def putByte(index, value)
      @data[index] = [value].pack("C")
    end
    def littleEndian
      @ord = LE
      self
    end
    def getShort(index)
      @data[index..-1].unpack(@ord::SHORT)[0]
    end
    def putShort(index, value)
      @data[index...index+2] = [value].pack(@ord::SHORT)
    end
    def getInt(index)
      @data[index..-1].unpack(@ord::INT)[0]
    end
    def putInt(index, value)
      @data[index...index+4] = [value].pack(@ord::INT)
    end
    def getLong(index)
      @data[index..-1].unpack(@ord::LONG)[0]
    end
    def putLong(index, value)
      @data[index...index+8] = [value].pack(@ord::LONG)
    end
    def getFloat(index)
      @data[index..-1].unpack(@ord::FLOAT)[0]
    end
    def putFloat(index, value)
      @data[index...index+8] = [value].pack(@ord::FLOAT)
    end
    def inspect
      "Buffer(%s)" % Codec.new.toHexdump(self, 0, @data.length, 3)
    end
  end
end

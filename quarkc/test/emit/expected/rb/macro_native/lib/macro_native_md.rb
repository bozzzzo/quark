module Quark
def self.macro_native_md; MacroNativeMd; end
module MacroNativeMd
require 'quark' # .../reflect
# for ('macro_native_md',): require_relative 'macro_native' # 0 () ()


def self.macro_native_Native_test_Method; MacroNativeNativeTestMethod; end
class MacroNativeNativeTestMethod < ::Quark.quark.reflect.Method



    def initialize()
        
        super("quark.void", "test", ::DatawireQuarkCore::List.new([]))

        nil
    end




    def invoke(object, args)
        
        obj = object
        obj.test()
        return nil

        nil
    end

    def _getClass()
        
        return nil

        nil
    end

    def _getField(name)
        
        return nil

        nil
    end

    def _setField(name, value)
        
        nil

        nil
    end

    def __init_fields__()
        
        super

        nil
    end


end

def self.macro_native_Native; MacroNativeNative; end
class MacroNativeNative < ::Quark.quark.reflect.QuarkClass
    extend ::DatawireQuarkCore::Static

    static singleton: -> { ::Quark.macro_native_md.macro_native_Native.new() }



    def initialize()
        
        super("macro_native.Native")
        (self).name = "macro_native.Native"
        (self).parameters = ::DatawireQuarkCore::List.new([])
        (self).fields = ::DatawireQuarkCore::List.new([])
        (self).methods = ::DatawireQuarkCore::List.new([::Quark.macro_native_md.macro_native_Native_test_Method.new()])

        nil
    end




    def construct(args)
        
        return ::Quark.macro_native.Native.new()

        nil
    end

    def _getClass()
        
        return nil

        nil
    end

    def _getField(name)
        
        return nil

        nil
    end

    def _setField(name, value)
        
        nil

        nil
    end

    def __init_fields__()
        
        super

        nil
    end


end
MacroNativeNative.unlazy_statics


def self.Root; Root; end
class Root < ::DatawireQuarkCore::QuarkObject
    extend ::DatawireQuarkCore::Static

    static macro_native_Native_md: -> { ::Quark.macro_native_md.macro_native_Native.singleton }



    def initialize()
        self.__init_fields__

        nil
    end




    def _getClass()
        
        return nil

        nil
    end

    def _getField(name)
        
        return nil

        nil
    end

    def _setField(name, value)
        
        nil

        nil
    end

    def __init_fields__()
        

        nil
    end


end
Root.unlazy_statics
end # module MacroNativeMd
end # module Quark

module Quark
require "quark"
def self.super; Super; end
module Super
require 'quark' # .../reflect
require_relative 'super_md' # 0 () ()
require_relative 'super' # 0 () ()


def self.A; A; end
class A < ::DatawireQuarkCore::QuarkObject
    attr_accessor :name
    extend ::DatawireQuarkCore::Static

    static super_A_ref: -> { ::Quark.super_md.Root.super_A_md }



    def initialize(name)
        
        self.__init_fields__
        (self).name = name

        nil
    end




    def greet()
        
        ::DatawireQuarkCore.print("Hello")

        nil
    end

    def _getClass()
        
        return "super.A"

        nil
    end

    def _getField(name)
        
        if ((name) == ("name"))
            return (self).name
        end
        return nil

        nil
    end

    def _setField(name, value)
        
        if ((name) == ("name"))
            (self).name = value
        end

        nil
    end

    def __init_fields__()
        
        self.name = nil

        nil
    end


end
A.unlazy_statics

def self.B; B; end
class B < ::Quark.super.A
    extend ::DatawireQuarkCore::Static

    static super_B_ref: -> { ::Quark.super_md.Root.super_B_md }



    def initialize()
        
        super("Bob")

        nil
    end




    def greet()
        
        method(:greet).super_method.call()
        ::DatawireQuarkCore.print(("I'm ") + ((self).name))

        nil
    end

    def _getClass()
        
        return "super.B"

        nil
    end

    def _getField(name)
        
        if ((name) == ("name"))
            return (self).name
        end
        return nil

        nil
    end

    def _setField(name, value)
        
        if ((name) == ("name"))
            (self).name = value
        end

        nil
    end

    def __init_fields__()
        
        super

        nil
    end


end
B.unlazy_statics

def self.call_main()
    self.main(::DatawireQuarkCore::List.new(ARGV))

    nil
end
def self.main(args)
    
    b = ::Quark.super.B.new()
    b.greet()


    nil
end

if __FILE__ == $0 then ::Quark.super.call_main() end

end # module Super
end # module Quark

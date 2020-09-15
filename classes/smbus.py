from __future__ import print_function # needs to be first statement in file   
   

class SMBus:
    
    __shared_state = {}
    __i2C_memory_map = {}  
    # and whatever else you want in your class -- that's all!
    
    'I2C/SMBus stub'
    def __init__(self, device, debug=0):
        self.__dict__ = self.__shared_state
        self.i2C_memory_map = self.__i2C_memory_map
        self.write_flag = False
        self.debug_print = debug
    
    def resetAllDevices(self):
        #simulates power cycling all I2C display devices
        self.__i2C_memory_map = {}

    def resetParticularDevice(self, address):
        #simulates power cycling all one particular display device as adddressed by address
        self.i2C_memory_map[address]= {}

        
    def write_byte_data(self, address, register, value):
        if self.debug_print:
            print("I2C write. address = {}, register = {}, value = {}".format(hex(address), hex(register), hex(value)))
        self.write_flag = True;
        if(address in self.i2C_memory_map):
            if(register in self.i2C_memory_map[address]):
                if self.debug_print:
                    print ("old value:{} , new value:{}".format(self.i2C_memory_map[address][register], value))
                self.i2C_memory_map[address][register] = value 
            else:
                if self.debug_print:
                    print ("new register:{}, with value:{}".format(hex(register), hex(value)))
                self.i2C_memory_map[address][register] = value
        else:
            if self.debug_print:
                print ("New address:{}, with new register:{}, with value:{}".format(hex(address), hex(register), hex(value)))
            self.i2C_memory_map[address] = {}
            self.i2C_memory_map[address][register] = value
    def read_byte_data(self, address, register):
        if(address in self.i2C_memory_map):
            if(register in self.i2C_memory_map[address]):
                return self.i2C_memory_map[address][register]
        return 0x00
    
    def resetWriteFlag(self):
        self.write_flag = False
    def getWriteFlagStatus(self):
        return self.write_flag
    
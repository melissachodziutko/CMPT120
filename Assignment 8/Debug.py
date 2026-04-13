class Device:
    def __init__(self, brand, battery):
      self.brand = brand
      self.battery = battery
      self.powered_on = False
    
    def power_on(self):
    #if device is not powered on, power it on and print
      #print "(brand) is powering on)
    #set powered_on to true
    #if device is powered on, tell em it is
    

    def info(self):
      #print out the brand and battery life of the device


class Phone(Device):
    def __init__(self, brand, battery, carrier):
      #call super init
      #save carrier
    
    def call(self):
     #print out a "i am calling using {carrier}"
    

class Laptop(Device):
    def __init__(self, brand, battery, ram):
      #call super and keep track of ram.
    
    def ramCheck(self):
    #check if ram is bigger than 4 gb
    #if it is, tell them theyre all set
    #if it's less, tell them they should upgrade!




def main():

#Create a generic device, phone, and laptop
#use all their functions

main()

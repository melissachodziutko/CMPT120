class Device:
    def __init__(self, brand, battery):
      self.brand = brand
      self.battery = battery
      self.powered_on = False
    
    def power_on(self):
        if self.powered_on:
            print(self.brand + "is powered on")
            self.powered_on = True
        else:
            print(self.brand + "is already on")
    

    def info(self):
        print(self.brand + self.battery)
      #print out the brand and battery life of the device


class Phone(Device):
    def __init__(self, brand, battery, carrier):
        super().__init__(brand, battery)
        self.carrier = carrier
      #call super init
      #save carrier
    
    def call(self):
        print(self.carrier + "I am calling using {carrier}")
     #print out a "i am calling using {carrier}"
    

class Laptop(Device):
    def __init__(self, brand, battery, ram):
        super().__init__(ram)
        self.ram = ram
      #call super and keep track of ram.
    
    def ramCheck(self):
        if ram >= 4:
            print(str(self.ram + "is bigger than 4 gb twin"))
            ram == 4
        else
            print(str(self.ram + "its time to upgrade lil folk"))
    #check if ram is bigger than 4 gb
    #if it is, tell them theyre all set
    #if it's less, tell them they should upgrade!




def main():
Device1 = ("Verizon Wireless Device", 32) 
Phone1 = ("iPhone", 256)
Laptop1 = ("Lenovo", 128)

Device1.powered_on
Device1.info
Device1.ramncheck

Phone1.powered_on
Phone1.info
Phone1.call

Laptop1.powered_on
Laptop1.info
Laptop1.ramCheck
#Create a generic device, phone, and laptop
#use all their functions

main()

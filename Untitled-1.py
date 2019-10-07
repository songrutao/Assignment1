class car:
    def __init__(self, interior, transmission, chassis, motor):
        self.interior = interior
        self.transmission = transmission
        self.chassis = chassis
        self.motor = motor

    def interior (self, input):
        self.interior = input
        print ("Color availabilaty: "% + self.interior)

    def transmission (self, input):
        self.transmission = input
        print ("transmission in this vehicle: "% + self.transmission)

    def chassis (self, input):
        self.chassis = input
      #  print "type of the chassis is: " self.chassis

    def motor (self, input):
        self.motor = input
    #    print "the motor is: " self.motor

Car1 = car("carbonfiber", 7, "a", "ss" )

Car1.interior()

#Car1.transmission()

#def main():
#    while (True):
#        selection = input("which car do you want to take a look( 1 - 3), otherwise exit this program (4)")
#        if (selection == 1)



Traceback (most recent call last):
  File "c:/Users/rutao/Desktop/Untitled-1.py", line 26, in <module>
    Car1.interior()
TypeError: 'str' object is not callable

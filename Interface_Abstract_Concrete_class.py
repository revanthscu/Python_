from abc import *
#interface 
class Vehicle(ABC):
    @abstractmethod
    def noOfWheels(self):
        pass
    def noOfDoors(self):
        pass
    def noOfExhaust(self):
        pass

    
#abstract class
class Bus(Vehicle):
    def noOfWheels(self):
        return 7
    def noOfDoors(self):
        return 2

    
#concrete class
class Completebus(Bus):
    def noOfExhaust(self):
        return 2

#object creation and calling
a=Completebus()
print(a.noOfWheels())
print(a.noOfDoors())
print(a.noOfExhaust())


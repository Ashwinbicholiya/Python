#Abstract class - 
#Abstract class and method does'nt have a body and the object class we can't 
#Declare a object to abtract class
#In Python we have to import ABC and anstractmethod t ocreate a abstract class

from abc import ABC , abstractmethod
class Computer(ABC): #Abstract class
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('Running')
    
Comp1 = Laptop()
Comp1.process()
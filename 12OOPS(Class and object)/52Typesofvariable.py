#There are two types of variable 
#1. Insatance variable  #2. Class(static) variable 

class car:
    wheel = 4  # class variable 

    def __init__(self):
        self.avg = 20     # instance variable
        self.com = "Audi"

c1=car() #car is constructor 
c2=car() 

c1.avg = 10  #we update thec1 average to 10

car.wheel = 5 #we update the car wheel to 5 

print(c1.avg, c1.com , c1.wheel)
print(c2.avg , c2.com , c2.wheel)

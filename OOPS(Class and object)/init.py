#In class there are : 1.atrributes and 2. Methods 
#Now wahts ia attributes or  variable 
#How to defne a variable 
#We have a special method for attributes 
#__init__(init means initialize)
#The init is automatically called for every object

class computer: 
    def __init__(self,cpu,ram): #We are accepting three values so self-comp1, cp-i5 and ram-8
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is " , self.cpu, self.ram)
        #why using self.cpu and self.ram
        #bcaz the cpu belong o the objects and self is an object(comp1)



comp1=computer("i5", 8) #in () we are passing comp1 by default
comp2 = computer("Ryzen 3", 4) # in () we are passing comp2 by default

comp1.config() 
comp2.config()

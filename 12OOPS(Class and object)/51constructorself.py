#1Size of an object 
#ans1.  Depsend on the no. of variables % size of anvariable
#2 Who allocatesbthe size to objects 
#Ans 2 - Constructor()
#program

class person:
    def __init__(self):
        self.name = "Ashwin"
        self.age = 2;0
    def update(self):
        self.age =20
    def compare(self,c2):
        if self.age == c2.age:
            return True
        else: 
            return False
 
c1 = person()  #person() is the constructor 
c2 = person()

c1.update()

if c1.compare(c2):  # c1 is self bcaz c1.compare so by default c1 is (self) 
    print("They are same") #if we define it by c2.compare then c2 is (self)
else:
    print("They are not same")

print(c1.name)
print(c2.name)


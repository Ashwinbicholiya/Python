#there are there types of method 
# 1.instance method 
#2. Class method 
#3 . Static method 

#1 . instance method 
class student:
    school = "ashwin" #class  veriable 

    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2  #instance variable 
        self.m3= m3 

    def avg(self):
        return(self.m1 +self.m2 + self.m3)/3
    #There are two types of instance 1> Accesor method 2> mutable method
#1>accessor methdo
    def get_m1(self):
        return self.m1

#These two method in instace are also called as getters and setters 
#2>Mutable method 
    def set_m1(self,value):
        self.m1 = value

s1=student(1,2,3)
s2=student(1,2,3)

print(s1.avg())


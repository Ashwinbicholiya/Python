#Constructor in inheritance 
#IMP - We use super() method to call init and also other methods 
class A:  #super class
    def __init__(self):   
        print(" Hey i am A")

class B(): # sub class
    def __init__(self):  #If you create object of sub class it will try find init of subclass
        print("Hey I am B")   #if inint is not found then it will call init of super class

class C(A,B): #sub class
    def __init__(self):
        super().__init__()  #if you have call super then iet will first call init of super class
        print("Hey i am C") #then call init of sub class

C1=C()  #IT FOLLOW THE MEETHOD OF METHOD RESOLUTION ORDER 
#MRO is follows from left to right means 
#IT will first check the super class of A then to B
#if init is found then it will print it and stop 
#if not foud then t will goes to B and call init of B


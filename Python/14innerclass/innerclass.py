#inner class 
#Class inside a class 
#1. -We can create object of inner class(Laptop) inside the outer  class(student)
#or
#2 . -we can create the object of inner class outside the outer class provided we use outer class

class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        ''' self.lap = self.laptop()'''  #1object of inner class inside a outer class

    def show(self):
        print(self.name , self.rollno)
        self.lap.show()
    #Inner  class 
    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.proc = "i5"
            self.ram = 8
        
        def show(self):
            print(self.brand , self.proc , self.ram)

s1=student("Ashwin", 30)
s2=student("Arjun" , 30)

#2outer class name(styudent) to call the inner class(laptop)
lap1 =student.laptop()
lap2 = student.laptop()

lap1.show()

'''s1.show()
s2.show()'''
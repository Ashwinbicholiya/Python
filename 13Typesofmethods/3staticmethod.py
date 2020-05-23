#3 Static method
#if we want a method which has nothing to do with instance method and class method 
#then we use static method 

class student:
    school="ashwin"
#for define static method we use @staticmehod  the define a method 
# which has no variable of class and instace 
    @staticmethod
    def info():
        print('Hello I am Ashwin')
#for calling
student.info()
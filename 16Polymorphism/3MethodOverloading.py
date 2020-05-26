#In python there is no concept of method overloading 
#Method overloading: 
#If you have a class and in that class you have a two methods with the same name but 
#different parametres or argument is called method overloading 

#In python we cant create a class with two same methods
#so We can do some tricks 

class student:     
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s 
s1=student()
print(s1.sum(5))
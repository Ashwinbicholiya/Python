#Method Overriding in python
#You have two methods with the same name and same arguments but in python we cant 
#create a two same methods in a same class
#We are using inheritance to inherit class a in b and in class b we have same method as in class a
#example

class A:
    def show(self):
        print('Show A')
    
class B(A):
    def show(self):
        print('Show B')

B1=B()
B1.show()
#Polymorphism -> Poly-Many and morph ism -> Forms
#Object will have multiple forms 
#We use this cocept in : 
#1-Loose coupling
#2- Dependecy injection 
#3 - Interface 
#There are four ways to implement the polymorphism
#1-Duck typing ,2- Operator Overloading ,3- Method overloading ,4-Method overloading
#1 - Duck typing 
# In python we have concept of dynamic typing like: 
# x=5, x="ashwin"  so in this we wont add this number ,x -int and x is also a type of character

class pycharm: 
    def execute(self):
        print('Compling')
        print('Running')
    
class laptop:
    def code(self,ide):
        ide.execute()

ide=pycharm()
lap1=laptop()
lap1.code(ide)

class A:
    def function1(self):
        print('function 1 working')
    def function2(self):
        print('function 2 working')
class B(A): #Single inheriance 
    def function3(self):
        print('function 3 working')
    def function4(self):
        print('function 4 working')
class C(B): #multilevel inheritace  
    def function5(self):
        print('Function 5 working ')

C1=C()
C1.function1()

#If B: 
# AND C(A,B) then it is multiple inheritance
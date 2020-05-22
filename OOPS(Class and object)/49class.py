#Class and object in python
#How we define a class :  Class Classname
#In classthere are :  1.- Attributes - Variables
#Behaviour - Methods(this are function but in class we called it methods)
#After that there are objects 

#Everything is object in Python

#Example

class computer:
    def config(self):
        print("i5 , 8GB RAM , 1TB")

comp1 = computer()
comp2 = computer()

#This is the first way to define a object 
'''computer.config(comp1)
computer.config(comp2)'''

#This is the second way to define a object 
#Mostly we use this way
comp1.config()
comp2.config()
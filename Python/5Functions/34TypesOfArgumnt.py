# 1 Position
'''def person(name,age):
    print(name)
    print(age)
#How we know that ashwin is going in name and 20 is going in age
#thats where position comes in 
person("Ashwin", 20) 

#What if we dont know the position 
#Then we use the Keyword'''

#2 Keyword 

'''def person(name,age):
    print(name)
    print(age)

person(name="Ashwin" , age= 20)
#or 
person(age=20, name= "Ashwin")'''

#3 Default

#what if want age as 18
#WE use default 

'''def person(name, age=18):
    print(name)
    print(age)
person("Ashwin")
#iF we pass age then it will upgrade the age from 18 to 20 
person("Ashwin",20)'''

#4 Variable length
#what if we want to add multiple variables 
#then we the variable length 
#*b is use to accept muliple values
#the multiple values are in the form of tuple 
#that why we use the loop to add one by one value in C
'''def add(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
add(1,2,3,4,5)'''
#we can pass the multiple values so (2,3,4,5) is tuple

#we can do this without a

def add(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
add(1,2,3,4,5,6,6,77)





  


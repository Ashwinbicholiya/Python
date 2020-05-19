#Que What is Recusion
#Ans Recusion means the function calling it self 
#example

'''def greet():
    print('Hello') 

    greet() #The function caling itself and there is no limit 
    #We have to define a limit to how many times that function is calling itself
    #If we dont define a limit then 
    #In python the function call itself at 1000 times is is default in python
greet()'''

#assign a limit to function

import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0
def greet():
    global i 
    i+=1
    print('Hello', i)
    greet()
    
greet()
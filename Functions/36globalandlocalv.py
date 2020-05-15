#Global and local Variable

#this is Global Variable
a=10 

#gl: global and local
#Local Variable a=9
def some():
    a=9
    #The scope of a is inside a function  
    print(a)
some()
#The scope of a is outside a function
print(a)

    



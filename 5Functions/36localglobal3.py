#What if want to use local and global both var. inside a function 

#We use globals()[] Function not a keyword

a=10
def some():
    a=9
    print(id(a)) #address  of local var a 
#we have to define a var. a because outside the function there are multiple var. 
    x=globals()['a'] 
    print('Inside function', a)

    globals()['a']= 15
    print(id(a)) #address of global var a is same as local var address

some()
print("Outside Function", a)
print(id(a))
#the address is changed 


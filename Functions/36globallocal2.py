#If we want to change the local var or use a global var in function
#Use global keyword
a=10
def some():
    global a  #use global and define varibale that you want to use 
    #When we define a as global so python can know that this is not a local var.. 
    #this will change the value of a to 15 as in function and outside the function
    a=15  
    print("Inside functions", a)

some()
print("Outside function", a)
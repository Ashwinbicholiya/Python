#Decorators: 
#Using the decoratos we can change the existing function without touching it
#Program : 
#Create a program that divide the two numbers with the help of funtions
#now condition is that if user enter the two value 
#if numerator is grate then denominator so gave divide it 
#if denominator is grater then numerator then swap the value and giv the output

#create function
#Now we change this existing function 
#we are using decorator : means create a new function
#using func we are changing the existing func.
#using this funnction we changing the value means swap this value  
 #return this func means we are returning the a,b value
 #we are assigning the div function to the new smart_div function
 #values


def div(a,b):
    print(a/b)
def smart_div(func): 
    def inner(a,b): 
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner 
div1 =smart_div(div) 
div1(2,4)   
        
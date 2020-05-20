#fliter map and reduce
#we are using filter , map and reduce function 
#program: create a list, fetch all the even numbers, double the even numbers
#and add +  all the doubles numbers 

from functools import reduce  #import reduce
nums=[3,4,5,6,7,8,9,10]

#fliter
evenno = list(filter(lambda n: n%2==0,nums))
print(evenno)

#Map
double = list(map(lambda n: n*2,evenno))
print(double)

#Reduce
#Reduce belongs to the functools, so we have to import it from the functools
sumall = reduce(lambda a,b: a+b ,double)
print(sumall)
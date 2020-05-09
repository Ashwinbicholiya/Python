from numpy import * 

# in logspace the gap between two is not fixed 
#the spacing between two no.
#would be depend upon the log of it
#is this is our conition (1,10,3)
#this will start from 10^1 to 10^10
#the diff. between the number of parts would be 3

arr= logspace(1,10,3)
print(arr[1],)
#convert 2 d array to 1 d array
#function use 
#flatten() 
#it will convert 2d or multi dimension array into 1d array

from numpy import * 

arr= array([
    [1,2,3,4],
    [5,6,7,8]
])

arr1=arr.flatten()

print(arr1)
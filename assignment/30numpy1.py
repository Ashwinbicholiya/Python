#find a max value of an array without using inbuilt function

from numpy import * 

arr1= array([1,8,1,55])
max=0
for i in range(len(arr1)):
    if arr1[i] > max : 
        max= arr1[i]
    else: 
        pass
print(max)  
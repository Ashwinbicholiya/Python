#create 3d array from 2d array
#function use reshape()

from numpy import * 

arr1=array([
    [1,2,3,4,5,6],
    [5,6,7,8,9,1]
])

arr2=arr1.flatten()

arr3=arr2.reshape(2,2,3)
print(arr3)

#we got 1 big 3d array which has 2 2d array and which has 2 single array 
#and then  which has 3 values 
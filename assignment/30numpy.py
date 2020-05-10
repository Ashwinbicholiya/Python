#add 2 arrays using forloop
from numpy import * 

arr1=array( [1,2,3,4])

arr2=array([1,2,3,4])

arr3= empty(4,int)

for i in range(len(arr1)):
    arr3[i] = (arr1[i] + arr2[i])
print(arr3)
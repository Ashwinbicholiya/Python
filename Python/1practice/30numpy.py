#add 5 in array
from array import * 

arr1 = array('i', [1,2,3,4,5])
arr2 = array('i' , [])

for i in range(len(arr1)):
    arr2.append(arr1[i] + 5)
print(arr2)
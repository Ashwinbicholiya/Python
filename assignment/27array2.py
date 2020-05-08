#Reverse array
from array import *

arr=array('i', [1,2,3,4,5])
arr2=array('i',[])

i=0
while(i<len(arr)):
    y=arr[len(arr)-1-i]
    arr2.append(y)
    i+=1
print(arr2)
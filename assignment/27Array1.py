#Delete the index value without using inbuilt function

from array import *

arr=array('i',[])
n=int(input('Enter the lenth of array : '))

for i in range(n):
    val=int(input('Enter the Next Values'))
    arr.append(val)
print(arr)

x=int(input('Enter the index number of value to delete the value : '))

for c in range(len(arr)):
    if c==x:
        pass
    else:
        print(arr[c])

    
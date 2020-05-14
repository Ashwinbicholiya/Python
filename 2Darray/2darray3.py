#convert 1d array to multi dimension array
# function use reshape()
#give row and columns
from numpy import * 

arr=array([1,2,3,4,5,6,7,8,9])

arr1=arr.reshape(3,3)
print(arr1)
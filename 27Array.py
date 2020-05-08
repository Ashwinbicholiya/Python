from array import *
#create array
arr=array('i', [])
n=int(input('Enter the length of Array : '))

for i in range(n):
    val=int(input('Enter the next Number : '))
    arr.append(val) #appen is used to add the value in  array
print(arr)

#for searching the value  and find the index of that value
x=int(input('Enter the value to find and index of that value : '))

k=0 #index number 
for e in arr:
    if e==x:
        print(k)
        break
    k+=1



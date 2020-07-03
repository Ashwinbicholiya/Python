from numpy import *  
A=array([
    [1,2,3],
    [4,5,6]
])

B=array([
    [7,8],
    [9,10],
    [11,12]
])
C=zeros(4, int).reshape(2,2)
print("Array A")
for i in range(2):
    for j in range(3):
        print(A[i][j], end=" ")
    print()

print("Array B")
for i in range(3):
    for j in range(2):
        print(B[i][j], end=" ")
    print()

sum=0

for i in range(2):
    for j in range(2):
        for k in range(3):
            sum= sum + A[i][k] * B[k][j]
        C[i][j] = sum
        sum=0

print("Final Matrix is")

for i in range(2):
    for j in range(2):
        print(C[i][j], end = " ")
    print()

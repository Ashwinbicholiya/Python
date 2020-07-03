#create matirx 
#Add two matrix
#functions in matrix
from numpy import * 

m=matrix('1 2 3 4 ; 5 6 7 8')
m1=matrix('1 2 3 4; 5 6 7 8')
print(m+m1)

#function 
# 1 : Daigonal  Functions

print(diagonal(m))

# 2 : Min and MAx function

print(m.min())
print(m.max())
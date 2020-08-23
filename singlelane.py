from itertools import permutations
import math
N = int(input())
Lists = list(map(int,input().split()))
l1=math.factorial(N)//math.factorial(N-(N))
l2=math.factorial(N)//math.factorial(N-(N-1))
perm=[]
perm.append(l1)
perm.append(l2)

if(N%2==0):
    total=sum(perm) +2
else:
    total=sum(perm)-1
print("%.6f"%(total/perm[-1]))

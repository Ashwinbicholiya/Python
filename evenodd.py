from itertools import product
l,h = input().split()
l,h = int(l),int(h)
if l>=0 and h>=0 and l<=h:
  k=int(input())
  perm = (i for i in product(range(l,h+1),repeat=k) if sum(i)%2==0)
  print(sum(1 for x in perm),end="")
l,h = input().split()
l,h= int(l),int(h)
k=int(input())
count=0
for i in range(l,h+1):
  if i%2==0:
    count+=1
total_num = h-l+1
print(total_num*(k-1)*count)
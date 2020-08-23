import sys
sys.stdout = open('TcsCodevita/output.txt', 'w')
sys.stdin = open('TcsCodevita/input.txt', 'r')
n,k =[int(x) for x in input().split()]
fact=[]
count=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        fact.append(i)
        fact.append(n//i)
    count+=2
fact.sort()
print(fact)
if count > k:
    print(fact[-k])
else:
    print(1)
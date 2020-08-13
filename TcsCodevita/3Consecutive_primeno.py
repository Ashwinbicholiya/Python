#input
20
#output
2

n = int(input())
prime = []
count = 0
prime =[i for i in range(2,n) if all(i%j!=0 for j in range(2,int(i**0.5)))]

for i in range(2,len(prime)):
    sum=0
    for j in prime:
        sum +=j
        if sum == prime[i]:
            count+=1
        if sum > prime[i]:
            break
print(count)
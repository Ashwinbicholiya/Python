#input 
1
4
1 2 3 4 5
#output 33

import sys
sys.stdout = open('TcsCodevita/output.txt', 'w')
sys.stdin = open('TcsCodevita/input.txt', 'r')

T = int(input())
res = []
for i in range(0,T):
    N= int(input())
    arr=[]
    candies = [int(x) for x in input().split()]
    candies.sort()
       while(len(candies)>= 2):
        candies.sort()
        sum1=candies[0]+candies[1]
        arr.append(sum1)
        candies.pop(0)
        candies.pop(0)
        candies.append(arr[-1])
    res.append(sum(arr))
for r in res:
    print(r)


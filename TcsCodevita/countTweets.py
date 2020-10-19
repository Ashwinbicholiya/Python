import sys
sys.stdout = open('TcsCodevita/output.txt', 'w')
sys.stdin = open('TcsCodevita/input.txt', 'r')

n,k = [int(x) for x in input().split()]
arr = [0]*n
for i in range(k):
    e = input()
    if e!='CLOSEALL':
        com,pos = [x for x in e.split()]
        if arr[int(pos)-1] ==1:
            arr[int(pos)-1]=0
        else:
            arr[int(pos)-1]=1
    else:
        arr=[0]*n
    print(arr.count(1))

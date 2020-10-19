import sys
sys.stdout = open('TcsCodevita/output.txt', 'w')
sys.stdin = open('TcsCodevita/input.txt', 'r')

n,m,r = [int(x) for x in input().split()]
N=[int(x) for x in input().split()]
M=[int(x) for x in input().split()]
inp=sum(N)
out=sum(M)
if(inp==out):
    print('BALANCED')
elif(inp!=out):
    diff=inp-out
    if(inp>out):
        diff=diff+r
        print(-diff)
    else:
        diff=(diff+r)
        print(diff)

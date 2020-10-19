import sys
sys.stdout = open('TcsDigital/output.txt', 'w')
sys.stdin = open('TcsDigital/input.txt', 'r')
n,m,r = [int(x) for x in input().split()]
N=[int(x) for x in input().split()]
M=[int(x) for x in input().split()]
inp=sum(N)
out=sum(M)
diff=inp-out
if(inp>out):
    diff=diff+r
    if(diff==0):
        print('BALANCED')
    else:
        print(-diff)
else:
    diff=(diff+r)
    if(diff==0):
        print('BALANCED')
    else:
        print(diff)

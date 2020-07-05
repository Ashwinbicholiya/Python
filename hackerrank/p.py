import sys
sys.stdout = open('hackerrank/output.txt', 'w')
sys.stdin = open('hackerrank/input.txt', 'r')

S, N = input(), int(input()) 
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
    
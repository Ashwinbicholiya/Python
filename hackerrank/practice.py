import sys
sys.stdout = open('hackerrank/output.txt', 'w')
sys.stdin = open('hackerrank/input.txt', 'r')
from itertools import permutations

s ,k =  input().split()
p = list(permutations(sorted(s),int(k)))
for i in p:
    print(''.join(i))
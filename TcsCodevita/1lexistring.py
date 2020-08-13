import sys
sys.stdout = open('TcsCodevita/output.txt', 'w')
sys.stdin = open('TcsCodevita/input.txt', 'r')
#input
"""3
polikujmnhytgbvfredcxswqaz
abcd
qwryupcsfoghjkldezvxbintma
ativedoc
qwryupcsfoghjkldezvxbintma
tivedoc"""

test = int(input())

for i in range(1, test+1):
    p=input()
    s=input()
    list1 = []
    for i in s:
        list1.append(p.find(i))
    list1.sort()
    for i in list1:
        print(p[i], end="")
    print()


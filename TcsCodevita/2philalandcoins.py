import sys
sys.stdout = open('TcsCodevita/output.txt', 'w')
sys.stdin = open('TcsCodevita/input.txt', 'r')
test = int(input())

for i in range(1,test+1):
    print(len("{0:b}".format(int(input()))))

"""input 
2
25
10"""
#output
5
4


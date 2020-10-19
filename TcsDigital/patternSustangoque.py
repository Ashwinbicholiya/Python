import sys
sys.stdout = open('TcsDigital/output.txt', 'w')
sys.stdin = open('TcsDigital/input.txt', 'r')

def complete_bracelet(seq):
    find =1
    guess=0
    max_len = len(seq)//2
    for x in range(2,max_len):
        if seq[0:x] == seq[x:2*x] :
            return find
    return guess
list1 = [int(x) for x in input().split()]
result = complete_bracelet(list1)
print(result)

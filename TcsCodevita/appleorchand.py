import sys
sys.stdout = open('TcsCodevita/output.txt', 'w')
sys.stdin = open('TcsCodevita/input.txt', 'r')


def modulo11(num):
    num = int(num)
    return num%11
num = input()
print(modulo11(num))






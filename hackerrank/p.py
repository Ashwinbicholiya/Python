import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

s = input()
vowels = 'AEIOU'
a,b = 0,0

for i in range(len(s)):
    if s[i] in vowels:
        a += len(s) -i
    else:
        b += len(s) - i

if a>b:
    print('Kevin', a)
elif a<b:
    print('Stuart', b)
else:
    print('Draw')
    
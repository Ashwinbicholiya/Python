import sys
sys.stdout = open('TcsDigital/output.txt', 'w')
sys.stdin = open('TcsDigital/input.txt', 'r')
from collections import Counter
a=[i for i in input()]
b=[i for i in input()]
al=a[-1] 
bl=b[-1]
if al=="s":
    al='South'
elif al=='w':
    al='West'
elif al=='n':
    al='North'
elif al=='e':
    al=East
if bl=='s':
    bl='South'
elif bl=='w':
    bl='West'
elif bl=='n':
    bl='North'
elif bl=='e':
    bl='East'
a.remove(a[-1])
b.remove(b[-1])
ca = Counter(a)
cb=Counter(b)
ca_max=max(ca.keys(),key=(lambda k: ca[k]))
ca_min=min(ca.keys(),key=(lambda k: ca[k]))
cb_max=max(cb.keys(),key=(lambda k: cb[k]))
cb_min=min(cb.keys(),key=(lambda k: cb[k]))
ca_diff=ca[ca_max]-ca[ca_min]
cb_diff=cb[cb_max]-cb[cb_min]
print(ca_diff,al,cb_diff,bl)

import sys
sys.stdout = open('TcsDigital/output.txt', 'w')
sys.stdin = open('TcsDigital/input.txt', 'r')
sum =0
menu = [80,130,100,80,90,110,120,140,70,80,130,160,70,60,40,50,30,40,160,150]
while(True):
    n=int(input())
    q=int(input())
    o=input().lower()
    sum=sum+menu[n-1]*q
    if o=='y':
        continue
    elif o=='n':
        break
print('Total Amount : '+str(float(sum))+' INR')

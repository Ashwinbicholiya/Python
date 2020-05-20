from Calc import * 

a=int(input('Enter the number a : '))
b=int(input('Enter the number b : '))

c=int(input('enter the number 1 : add, 2 : sub, 3: mul , 4: divide'))
if c==1:
    print(add(a,b))
elif c==2:
    print(sub(a,b))
elif c==3:
    print(mul(a,b))
elif c==4:
    print(div(a,b))
else:
    print('Enter the correct number ')


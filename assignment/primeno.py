num = int(input('Enter a number : '))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num, 'Not a Prime Number ')
            break
    else:
        print(num , 'Prime Number')
else:
    print(num, 'Not a Prime Number')    
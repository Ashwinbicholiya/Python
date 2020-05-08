x=int(input('Enter a number : '))

if x==2 :
    print('Prime number')
elif x>1: 
    for i in range(2,20):
        if x%2==0:
            print(x, 'Not a prime number ')
            break
        else:
            print(x, 'Prime number ')
            break
elif x<=1:
    print(x, 'Not a Prime Number')

        
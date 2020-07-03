
def fact(x):
    if x<0:
        print('Number is zero or less then 1')
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
x=int(input('Enter a number '))
result = fact(x)

print(result)

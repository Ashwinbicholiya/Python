# Factroial using recursion
def fact(x):
    if x==0:
        return 1
    return x *fact(x-1)

x=int(input('Enter the number : '))
result = fact(x)
print(result)
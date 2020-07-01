#Enter the number from user and print the fibonacci number till that number 
#or less than that number with the help of functions
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c<n:
                print(c)

n=int(input('Enter the fibonacci number you want : '))
fib(n)
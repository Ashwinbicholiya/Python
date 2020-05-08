x=int(input("enter a number"))
r = x%2

if r==0:
    print("even")
    if x>5:
        print("greater")
    else:
        print("n")
else:
    print("odd")
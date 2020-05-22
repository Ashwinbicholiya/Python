
n=int(input('Enter the number of length of list : '))
lst=[]

for i in range(n):
    vals=int(input('Enter the values : '))
    lst.append(vals)
print(lst)

def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd = count(lst)

print("Even : {} and Odd : {} ".format(even,odd))

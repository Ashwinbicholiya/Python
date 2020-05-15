#How to pass parameter in function and what happen with the value and different types of
# Parameter and agrrement We can pass

#1
'''def update(x):
    x=8
    print(x)
update(10)'''

#2
'''def update(x):
    x=8
    print(x)
a=10
update(a)
print(a)'''

#3
'''def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x", x)

a=10
print(id(a))
update(a)
print("a", a)'''

#4
def update(x):
    print(id(x))
    x[1] = 25
    print(id(x))
    print("x",x)
lst=[10,20,30]
print(id(lst))
update(lst)
print("lst", lst)

#List is mutable(changeable) 
#that why all the address is same and original list is updated 
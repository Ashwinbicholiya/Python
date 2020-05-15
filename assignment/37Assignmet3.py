# Que.Take ten names from the user and then count and display the number of users
# Who has length more then Five letters 

n=int(input("Enter the numbers of Users : "))
lst=[]

for i in range(n):
    lst.append(input('Enter the user name : '))
print(lst)

lst1=[]
c=0
for i in lst:
    if len(i)> 5 :
        lst1.append(i)
        c+=1
print("no. of user whose name is > 5 is : ",c)
print(lst1)
        




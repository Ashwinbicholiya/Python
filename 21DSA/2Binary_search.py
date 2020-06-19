pos=-1

def search(list,n):
    l = 0
    u = len(list) -1

    while l<=u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l=mid+1
            else:
                u=mid-1
    return False
list=[]
a=int(input('Enter the length of list : '))

for i in range(a):
    val=int(input('Enter the Values : '))
    list.append(val)
n=14

if search(list,n):
    print('No. found at ',pos+1)
else:
    print('No. Not Found')
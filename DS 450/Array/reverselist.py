#1) Initialize start and end indexes as start = 0, end = n-1 
#2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
#start = start +1, end = end – 1

def reverselist(A,start,end):
    while start < end:
        A[start],A[end] = A[end], A[start]
        start +=1
        end -=1
A=[1,2,3,4,5,6]
print(A)
reverselist(A,0,len(A)-1)
print('Reverse List is ')
print(A)


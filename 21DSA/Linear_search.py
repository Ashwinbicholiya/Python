pos = 1
def Search(list, n):
    for i in range(len(list)):
        if list[i] ==n:
            globals()['pos'] = i
            return True 
    return False

list = [8,4,6,7,4]
n = 7

if Search(list, n):
    print('Found at ',pos+1)
else:
    print('Not Found')
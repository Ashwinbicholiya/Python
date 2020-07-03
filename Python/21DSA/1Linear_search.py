pos = -1

def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False
list = [3,4,6,32,18,6,7,12]
n=18

if search(list, n):
    print('No. Found at', pos+1)
else:
    print('No. Not Found')
from pythonds.basic.stack import Stack

def divides(decimalnumber):
    rem_stack = Stack()
    while decimalnumber > 0:
        remainder = decimalnumber % 2
        rem_stack.push(remainder)
        decimalnumber = decimalnumber // 2

    bin_string = ''
    while not rem_stack.isEmpty():
        bin_string = bin_string + str(rem_stack.pop())  
    return bin_string      

print('233 is ',divides(233))
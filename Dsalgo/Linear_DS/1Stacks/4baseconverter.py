from pythonds.basic.stack import Stack

def baseconverter(decNumber,base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()

    while decNumber>0:
        rem = decNumber % base
        rem_stack.push(rem)
        decNumber = decNumber // base
    
    newString = ''
    while not rem_stack.isEmpty():
        newString = newString + digits[rem_stack.pop()]
    
    return newString

print('Binary: ',baseconverter(24,2))
print('octal : ',baseconverter(26,8))
print('hex   : ',baseconverter(26,16))

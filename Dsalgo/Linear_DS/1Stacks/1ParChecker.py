from pythonds.basic.stack import Stack

def checker(StringSymbol):
    s = Stack()
    Balanced = True
    index = 0
    while index < len(StringSymbol) and Balanced:
        symbol = StringSymbol[index]
        if symbol in '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
        index = index + 1
    
    if Balanced and s.isEmpty():
        return True
    else:
        return False
    
print(checker('((()))'))
print(checker('(()'))


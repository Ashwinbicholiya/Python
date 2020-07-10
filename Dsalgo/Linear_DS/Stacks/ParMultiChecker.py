from pythonds.basic.stack import Stack

def checker(SymbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(SymbolString) and balanced:
        symbol = SymbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            top = s.pop()
            if not matches(top,symbol):
                balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open,close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(checker('(({}[]))'))
print(checker('(([(]{}()'))
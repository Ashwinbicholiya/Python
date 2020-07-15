from pythonds.basic.deque import Deque

def palchecker(astring):
    a = Deque()
    for ch in astring:
        a.addRear(ch)
    StillEqual = True

    while a.size() > 1 and StillEqual:
        first = a.removeRear()
        last = a.removeFront()

        if first != last:
            StillEqual = False 
    return StillEqual

print('palchecker(radar) ->',palchecker('radar'))
print('palchecker(Newer) ->',palchecker('newer'))
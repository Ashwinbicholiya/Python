from pythonds.basic.queue import Queue

def hotpotato(namelist,num):
    aqueue = Queue()
    for name in namelist:
        aqueue.enqueue(name)
    
    while aqueue.size() > 1:
        for i in range(num):
            aqueue.enqueue(aqueue.dequeue())
        aqueue.dequeue(),
    return aqueue.dequeue()

print(hotpotato(['Bill','David','Susan','Jame','kent','Brad'],7))
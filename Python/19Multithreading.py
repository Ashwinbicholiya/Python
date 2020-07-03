from time import *
from threading import *   #main thread divide into two thread that is t1 and t2 
class Hello(Thread):
        def run(self):
            for i in range(5):
                print('Hello')
                sleep(1) #stop for 1 second 

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)   #stop for 1 second 

t1=Hello()
t2=Hi()

t1.start()
sleep(0.2)   #stop for 0.2 second 
t2.start()



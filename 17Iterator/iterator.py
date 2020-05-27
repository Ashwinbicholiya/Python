#Iterator : (++)
#There is method is call iter and next
#Iter will give the object
#Next will give the next object

'''nums = [1,2,3,4]
it=iter(nums)
print(it.__next__())
print(next(it))'''

class topten:
    def __init__(self):
        self.num =1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num +=1

            return val
        else:
            raise StopIteration

values = topten()
print(next(values))  #This will print 1
for i in values: #This will print after the (bcaz iter save 1 value)1 valuethat is 2 and then goes  till 10
    print(i)
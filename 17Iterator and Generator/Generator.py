#generator:
#Instead of using iterator we acn use generator 
#Generator can get te iterator and we dont have to call iter() method 

#W use Yield to get the value 

#Print topten perfecr square value using generator

def topten():
    n=1

    while n<=10:
        sq = n*n
        yield sq
        n +=1
    
values = topten()
 
for i in values:
    print(i)

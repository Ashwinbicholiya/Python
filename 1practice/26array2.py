from array import *

vals=array('i', [2,3,5,7,6,8])

newArr= array(vals.typecode , (a for a in vals))

for i in newArr:
    print(i)
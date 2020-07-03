#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(nums):
    sum_num = 0
    for i in nums:
        sum_num = sum_num + i

    average = sum_num / len(nums)
    return average
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
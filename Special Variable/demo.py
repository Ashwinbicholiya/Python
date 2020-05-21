#1 
''' . #Special variable __name__
#In other languages the main is the starting point of the executin
#in Python the we name uderscore variable as a starting point of execution
#Example:

#print(__name__)
#output: __main__

#in project there are lots of modules like lots of files
#There will be some modules we will run first'''

#2

import calc 
print('Demo : ' + __name__)

'''We are importing cac in this demo module so calc execute and then demo execute'''
'''calc gives output : Hello calc
because we are importing it '''
'''Demo givs the : Demo main'''




'''#For differet types of error we have different except error like (ValueError) & (zeroDivisionError)

#What if there is an error we dont know about

#we use except Exception as e and print(e)'''

'''#Final block
#It will be executed if we get error as well as if we dont get the error 
#Syntex is 
#finally: code...'''
'''a=6
b=0

try:
    print(a/b)
except Exception as e:
    print('You can not divide a no. by ero',e)
finally:  
    print('Bye')'''
#if user enter the charatcter instead of number
#As a developer we have to except it and give user a output instead of error
try:
    a=int(input('Enter the no : '))
except ValueError as e:
    print('You entered a character', e)


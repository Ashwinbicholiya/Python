#lamda: Fliter
#Example : Create a list and fetch all the even number present in the list
#Create a list
#fliter take two arguments
nums=[3,4,5,6,7,8,9,10]

evenno = list(filter(lambda n: n%2==0,nums))

print(evenno)
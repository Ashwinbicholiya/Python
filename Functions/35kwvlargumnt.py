#Keyword variable length argument

def person(name,**data):
    print(name)

    for i,j in data.items():
        print(i,j)

person('Ashwin', age=20, city='Indore', Contact=98277)

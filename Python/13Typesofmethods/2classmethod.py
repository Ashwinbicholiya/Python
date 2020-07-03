#2 Class method 
#in Instance method we are working with the instance variable only 
#in class method we are working with the class variable 

class student:
    school = "Ashwin"

#for using the class method , we need to use decorators 

    @classmethod 
    def info(cls): #for class method we using cls instead of self
        return cls.school

print(student.info())
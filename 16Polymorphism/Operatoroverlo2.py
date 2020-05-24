class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2 
    
    def __gt__(self,other): #Greater then
        r1=self.m1 + self.m1
        r2=other.m2 + other.m2
        if r1 > r2:
            return True
        else: 
            return False
        
s1=student(2,4)
s2=student(6,-1)

if s1 > s2 :
    print('S1 wins ')
else : 
    print('s2 wins')
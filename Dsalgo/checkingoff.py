#Anagram Solution
#O(n^2)
def anagram(s1,s2):
    if len(s1)!=len(s2) : return False #quick test if fail
    n = len(s1)  #1 countdown to list
    s2_list = list(s2) #1 convert  to list
    
    for c1 in s1:  #n
        for i in range(len(s2_list)): #n squared
            if c1 == s2_list[i]:  #n squared
                s2_list[i] == None  #(0 to n squared)  check off
                n -= 1 # n squared -remove from count
                break  # found c1, just to next one 
    return n==0  # found all the needed numbers
# 2 + n + n^2 + n^2 = 2n^2 +n + 2 = O(n^2) -> we can say that 
s1,s2 = input(), input()
print(anagram(s1,s2))

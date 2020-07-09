#Anagram solution
def anagram(s1,s2):
    n = len(s1)
    if n!= len(s2): return False
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()  # n logn
    list2.sort()

    for i in range(n):
        if list1[i]!= list2[i]: return False
    return True
s1, s2 = input().strip().split()
print(anagram(s1,s2))
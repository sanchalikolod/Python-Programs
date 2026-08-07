#Checking for anagrams.

def anagrams(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        c1=0
        c2=0
        for j in range(len(s2)):
            if s1[i]==s1[j]:
                c1=c1+1
            if s1[i]==s2[j]:
                c2=c2+1
        if c1!=c2:
            return False
    return True

s1=input("Enter first word: ")
s2=input("Enter second word: ")
result=anagrams(s1,s2)
print("Are the words anagrams? ",result)

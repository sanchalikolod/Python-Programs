#Find all pairs in list whose sum equals the target.

lst=[0,5,2,1,3,4]
print("List: ",lst)
target=int(input("Enter your target: "))
print("Pairs which give addition as",target,"are:")

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==target:
            print(lst[i],"+",lst[j],"= 5")

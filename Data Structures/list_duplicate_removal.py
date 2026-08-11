#Print duplicate elements of a list only once.

lst=[1,2,3,5,67,8,3,2,67,9]
printed=[]
print("The list is: ",lst)
print("List without duplicate elements: ")
for i in lst:
    if lst.count(i) and i not in printed:
        printed.append(i)

print(printed)

#Find the first non-repeating element of the list:

lst=[2,2,3,3,3,1,5,78]
print("List: ",lst)
print("The first non-repeating element of the list: ")
for i in lst:
    if lst.count(i)==1:
        print(i)
        break

#Find the second largest element in a list.

lst=[10,45,4,99,68]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp

print("The list is: ",lst)
print("Second largest element of the list is: ",lst[-2])

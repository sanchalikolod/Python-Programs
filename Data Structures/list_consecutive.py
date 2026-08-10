#Find the element that appears consecutively the maximum number of times.

lst = [1, 2, 2, 2, 3, 3, 1]

max_count = 0
element = 0

for i in range(len(lst)):
    count = 1

    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            count += 1
        else:
            break

    if count > max_count:
        max_count = count
        element = lst[i]
        
print("List: ",lst)
print("Element =", element)
print("Count =", max_count)

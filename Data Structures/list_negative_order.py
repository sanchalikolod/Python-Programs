#Move all negative numbers to the beginning while maintaining order.

lst = [3, -2, 5, -7, 8, -1]

result = []

for i in lst:
    if i < 0:
        result.append(i)

for i in lst:
    if i >= 0:
        result.append(i)

print("Original list: ",lst)
print("List with negative numbers at beginning: ",result)

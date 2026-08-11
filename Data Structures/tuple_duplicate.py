#Remove the duplicate tuples while maintaining order.
lst = [(1, 2), (3, 4), (1, 2), (5, 6)]

result = []

print("List of tuples: ",lst)

for t in lst:
    if t not in result:
        result.append(t)

print("List after removing duplicates: ")
print(result)

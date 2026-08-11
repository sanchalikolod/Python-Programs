#Count the unique tuples in the list:

lst = [(1, 2), (3, 4), (1, 2), (5, 6)]

unique = []

for t in lst:
    if t not in unique:
        unique.append(t)

print("List of tuples: ",lst)
print("Count of unique tuples: ",len(unique))

#Print all numbers missing for 1 to N.

lst = [1, 2, 4, 6, 8]
N = 10

print("List: ",lst)
print("Value of N: 10")
print("Missing numbers:")
for i in range(1, N + 1):
    if i not in lst:
        print(i)

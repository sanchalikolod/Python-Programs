#Find symmetric difference in 2 sets without using function.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Set A: ",A)
print("Set B: ",B)

result = set()

for i in A:
    if i not in B:
        result.add(i)

for i in B:
    if i not in A:
        result.add(i)

print("Symmetric difference of the two sets: ",result)

#Print all even numbers of the list first and then odd numbers.

lst = [3, 4, 7, 2, 5, 8]

result = []

for i in lst:
    if i % 2 == 0:
        result.append(i)

for i in lst:
    if i % 2 != 0:
        result.append(i)

print(result)

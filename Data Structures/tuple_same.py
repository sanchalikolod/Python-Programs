#Check whether two tuples have same elements.
t1 = (1, 2, 3)
t2 = (3, 2, 1)

print("Tuple 1: ",t1)
print("Tuple 2: ",t2)

if sorted(t1) == sorted(t2):
    print("Same elements")
else:
    print("Different elements")

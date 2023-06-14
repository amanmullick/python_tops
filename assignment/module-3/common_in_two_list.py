"""Write a Python function that takes two lists and returns true if they have
at least one common member."""

lst1 = [1,22,33,44,00]
lst2 = [1,00,23,43]

for i in lst1:
    for j in lst2:
        if j==i:
            print("common",j)
            
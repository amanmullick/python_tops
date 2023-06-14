"""#a Python program to unzip a list of tuples into individual lists.
l=[(1,2),(99,11),(22,33)]
print(list(zip(*l)))

l = dict(l)
print(l)"""

#a Python program to unzip a list of tuples into individual lists.
l=[(1,2),(),(22,33)]
for i in l:
    for j in i:
        print(j)

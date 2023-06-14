#a Python program to replace last value of tuples in a list.
tup = (1,2,3)
lst = [4,5,6]

x=len(lst)-1
y=len(tup)-1

lst[x]=y
print(lst)
print(tup)
print()
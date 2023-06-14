"""Write a Python function to get the largest number, smallest num and sum of all from a list."""

lst = [11,22,33,44,66]

largest = max(lst)
smallest = min(lst)

sum = 0

for i in lst:
    sum = sum+i

print("largest : ",largest)
print("smallest : ",smallest)
print("sum of all numbers : ",sum)    
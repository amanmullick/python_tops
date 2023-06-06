"""Write a Python function to reverses a string if its length is a multiple of 4."""

n = input("enter : ")
l=len(n)
if l%4==0:
    print(n[::-1])
    
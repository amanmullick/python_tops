"""Write a Python program to count the number of characters (character
frequency) in a string"""

st = input("enter the string : ")
a=0

for i in st:
    a+=1
print(f"number of characters in {st} : {a}")
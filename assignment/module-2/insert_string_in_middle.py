"""• Write a Python function to insert a string in the middle of a string."""
s = input("enter string : ")
l = len(s)

ns = input("enter new string to be inserted : ")

c = int(l/2)

print(c,s[c])
print(s[0:c]+ns+s[c:])
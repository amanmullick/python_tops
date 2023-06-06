"""Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string."""

s = input("enter the string : ")

n = s.index("not")
p = s.index("poor")

print(n,p)

if p > n:
    s1=s.replace(s[n:(p+4)],"good")
print(s1)
"""Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of strings."""

lst = ["aman","ravi","pranav","krish","a"]
c=0
for i in lst:
    if len(i)>=2:
        c+=1

for j in lst:
    print("aa=",j[0])
"""Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
"""
st1=input("enter the first string : ")
st2=input("enter the second string : ")

st=st1

st3=st1.replace(st1[0:2],st2[0:2])
st4=st2.replace(st2[0:2],st[0:2])

print(st3)
print(st4)
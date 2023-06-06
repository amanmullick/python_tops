"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged."""

str1 = input("enter the string : ")
str1.lower()
l=len(str1)
print(l)

if l>=3:
    if str1.endswith("ing")==True:
        str1 = str1+"ly"
    else:
        str1 = str1+"ing"

print(str1)

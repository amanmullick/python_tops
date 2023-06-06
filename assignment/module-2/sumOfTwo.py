'''Write a Python program to sum of three given integers. However, if two
values are equal sum will be zero.'''

a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))

sum=0

if a==b or b==c or a==c:
    print(f"sum = {sum}")
else:
    sum=a+b+c
    print(f"sum = {sum}")
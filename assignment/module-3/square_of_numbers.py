"""Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30."""


for i in range(1,31):
    for j in range(1,31):
        if ((i*i) + (j*j))<=30:
            
            print()
            print("(",i,j,")",i*i ,"+", j*j ,"=", (i*i) + (j*j))
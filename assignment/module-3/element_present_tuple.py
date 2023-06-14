#a Python program to check whether an element exists within a tuple

tup = (1,2,3,4,5)

ele = input("enter element to be searched : ")
ele = int(ele)

if ele in tup:
    print("present")
else:
    print("not present")

"""Write a Python function that takes a list of words and returns the length of the longest one."""

n = int(input("enter the size of list : "))
lst=[]
for i in range(0,n):
    ele = input(f"enter number {i+1} element : ")    
    lst.append(ele)
c=0
print(lst)

print(max(lst))

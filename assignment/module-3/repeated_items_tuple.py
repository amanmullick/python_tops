#a Python program to find the repeated items of a tuple.

tup = (1,1,1,2,3)

tup=list(tup)
lst = tup.copy()

ll=[]
ee=[]
for i in lst:
    if i not in ll:
        ll.append(i)
    elif i in ll:
        ee.append(i)

print(ll)
print(ee)
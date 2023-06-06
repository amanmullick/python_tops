str = input("enter string : ")
print(str)
str=str.lower()
c=0
l = len(str)
print(l)
for i in str:
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        c+=1
        print("xx",c)
print(c)
if c>=l:
    print("vowel")
else:
    print("consonent")


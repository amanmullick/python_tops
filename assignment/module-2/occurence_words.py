"""Write a Python program to count the occurrences of each word in a given sentence"""
st = input("Enter the string : ")
for i in set(st):
    c = st.count(i)
    print(f"the occurrence of {i} : {c}")
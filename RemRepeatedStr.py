str=input("Enter a string\n")
lst=[]
for i in str:
    if(i not in lst):
        lst.append(i)

print("".join(lst))

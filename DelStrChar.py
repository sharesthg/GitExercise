str=input("Enter a String\n")
val=input("Enter value to be removed\n")

lst=[]
for i in str:
    if(i!=val):
        lst.append(i)

str="".join(lst)
print(str)

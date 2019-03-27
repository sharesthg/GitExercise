n=int(input("Enter the total number of list elements\n"))
lst=[]
for i in range(n):
    val=int(input("Enter a value\n"))
    lst.append(val)

lst2=[]
for i in lst:
    if(i not in lst2):
        lst2.append(i)

print(lst2)

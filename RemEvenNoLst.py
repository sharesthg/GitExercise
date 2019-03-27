n=int(input("Enter the total number of elements in the list\n"))
lst=[]
for i in range(n):
    val=int(input("Enter a value: "))
    lst.append(val)

for i in lst:
    if(i%2==0):
        lst.remove(i)

print(lst)

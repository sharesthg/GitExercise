n=int(input("Enter total no. of elements in the list\n"))
l=[]
for i in range(n):
    val=int(input("Enter a value\n"))
    l.append(val)

max=l[0]
for i in l:
    if(i>max):
        max=i

print(max)

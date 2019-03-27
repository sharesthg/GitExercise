n1=int(input("Enter total elements in list1\n"))
lst1=[]
for i in range(n1):
    val=int(input("Enter a value\n"))
    lst1.append(val)

n2=int(input("Enter total elements in list2\n"))
lst2=[]
for i in range(n2):
    val=int(input("Enter a value\n"))
    lst2.append(val)

for i in lst1:
    if(i in lst2):
        print(i)
        
    

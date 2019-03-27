n=int(input("Enter a number\n"))
l=[]
for i in range(n):
    val=int(input("Enter a value\n"))
    l.append(val)

print(l)

mul=1
for i in l:
    mul*=i

print(mul)

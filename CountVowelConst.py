str=input("Enter a string\n")
count1=0
count2=0
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count1+=1
    else:
        count2+=1

print("Vowels = {}, Consonents = {}".format(count1, count2))

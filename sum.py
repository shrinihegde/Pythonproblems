str=input("enter the numbers with space")
lst=str.split()
sum=0
for i in lst:
    sum=sum+int(i)
print("sum=",sum)
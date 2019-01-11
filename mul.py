str=input("enter the numbers with space: ")
lst=str.split()
mul=1
for i in lst:
    mul=mul*int(i)
print("mul=",mul)

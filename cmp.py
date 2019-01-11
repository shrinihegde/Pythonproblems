a=input("enter the some randomm number: ")
b=input("enter the same random number: ")
c=[int(i) for i in a.split()]
d=[int(j) for j in b.split()]
print(c)
print(d)
n=len(c)
m=len(d)
for i in range(n):
    for j in range(m):
        if c[i]==d[j]:
            print('True')

        

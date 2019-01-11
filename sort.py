a=input("enter the  random nnumbers: ")
b=[int(i) for i in a.split()]
n=len(b)-1
while n!=0:
    for j in range(n):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
        n=n-1
print(b)

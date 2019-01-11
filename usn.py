n=eval(input("enter the number of key value pairs: "))
lst1=[]
lst2=[]
for i in range(n):
    k=input("key %d: "%(i+1))
    l=input("value %d: "%(i+1))
    lst1.append(k)
    lst2.append(l)
    d=dict(zip(lst1,lst2))
print(d)

d={'a':"Hello",'b':"hey",'c':"hi"}
lst1=[]
lst2=[]
lst3=[]
n=eval(input("enter the number of additional entries: "))
for i in range(n):
    k=input("enter %d key: "%(i+1))
    lst2.append(input("enter %d value: "%(i+1)))
for key in d:
    if k!=key:
        a=lst1.append(k)
        lst3.append(a)
print(lst2)
print(lst1)
print(lst3)
d1=dict(zip(lst1,lst2))
print(d1)
d.update(d1)
print(d)

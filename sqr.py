n=eval(input("enter the number of key value pairs: "))
lst1=[]
lst2=[]
for j in range((n)):
    lst1.append(j)
    a=lst1[(j)]**2
    lst2.append(a)
    d=dict(zip(lst1,lst2))
print(d)

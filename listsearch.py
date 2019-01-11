a=input("enter the list items: ")
lst=a.split()
print(lst)
b=input("enter the search item: ")
for i in range(len(lst)):
    if b ==lst[i]:
        print(True)
    else:
        print(False)
    

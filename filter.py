def filter():
    lst=[]
    even=[]
    lst.extend(eval(input("enter the numbers into the list: ")))
    for i in range(len(lst)):
        if lst[i]%2==0:
            even.append(lst[i])
    print(even)
filter()

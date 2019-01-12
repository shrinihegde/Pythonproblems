#efining a function to add the numbers in the list
def sum():
#create an empty list and take the input into the list
    lst=[]
    lst.extend(eval(input("enter the numbers to be added: ")))
    sum=0
    for i in range(len(lst)):
        sum=sum+lst[i]
    print(sum)
sum()

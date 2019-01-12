#function to add the names to the list
def add(name):
    #create an empty list
    lst=[]
    #using the string format split the names and add it to the list
    lst=name.split()
    print(lst)
#get the input name to be added
a=input("enter the name to be appended: ")
#function call
add(a)


mydic={1:"speckbit",2:"world",3:"quiet"}
a=mydic.items()
search=input()
for i in a:
    if search==i[1]:
        print("key is ",i[0])
    

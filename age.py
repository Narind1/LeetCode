c=int(input("Enter the current age:"))
if(c<90):
    age=90-c
    weeks=age*52
    print(f"Weeks left:{weeks}")
else:
    print("Be happy you are alive")
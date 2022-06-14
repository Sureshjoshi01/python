
count = 0 
str = "y"
while str.upper() == "Y":
    name = input("Enter name whom you want to invite : ")
    print(name , "has now been invited ")
    count = count+1 
    str = input("Do you want to invote somebody else(Y/N) : ")  
    
    

print("Number of people invited to party : ", count)
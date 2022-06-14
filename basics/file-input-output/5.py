print("MENU\n")
print("1) Create a new file")
print("2) Dispaly the file")
print("3) Add a new item to the file ")
choice = int(input("Enter your choice "))
if choice == 1:
    sub = input("Enter a School subject ")
    file = open("Subject.txt","w")
    file.write(sub)
elif choice == 2:
    file = open("Subject.txt","r")
    print(file.read())
elif choice == 3:
    sub = input("Enter a new School subject ")
    file = open("Subject.txt","a")
    file.write("\n")
    file.write(sub)
    file = open("Subject.txt","r")
    print(file.read()) 
else:
    print("Not Supported")
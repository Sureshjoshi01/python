name = input("Enter First Name : ")
x = len(name)
if x < 5:
    sname = input("Enter Surname : ")
    jname = name+sname
    uname = jname.upper()
    print("Full Name : ", uname)
else:
    lname = name.lower()
    print(lname)
    
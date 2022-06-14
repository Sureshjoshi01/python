p1 = input("Enter new password : ")
p2 = input("Enter password again : ")
if p1 == p2:
    print("Thank You !")
elif p1.lower() == p2.lower():
    print("They must be in same case")
else:
    print("incorect")
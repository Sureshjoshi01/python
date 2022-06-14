total = 0
print("Enter 5 numbers : ")
for i in range(1,6): 
    n = int(input("Enter number : "))
    str = input("Do you want number to be included(yes/no) : ")
    if str.upper() == "YES":
        total = total+n
    elif str.upper() == "NO":
        quit

print("total = ", total)

             


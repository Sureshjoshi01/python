n1 = int(input("Enter a number : "))
n2 = int(input("Enter another number : "))
total = n1+n2 
str = "y"
while str.upper() == "Y":
    n = int(input("Enter number to be added : "))
    total = total+n
    str = input("Do you want to add another number(Y/N) : ")
print("Total is : ", total)
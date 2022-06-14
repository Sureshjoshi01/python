str = 'Y'
while str.upper() == 'Y':
    n = int(input("Enter a number b/w 10 and 20 : "  ))
    if n<10:
        print("Too low ")
        str = input("Do you want to continue(Y/N) : ")
    elif n>20:
        print("Too High ")
        str = input("Do you want to continue(Y/N) : ")
    else:
        print("Thank You")
        str = 'N'

# Program to check number is Odd Or Even

num = input("Enter a number : ")
check = input("Enter second number : ")
again = True
while again == True: 
    if num.isdigit() != True:
        num = input("You did not enter digit in first number, Enter first number again : ")
    elif check.isdigit() != True:
        check = input("You did not enter digit in second number, Enter second number again : ")
    elif (int(num) % int(check)) == 0:
        print(f'{num} is evenly divided by {check}')
        again = False 
    else:
        num = int(num)
        if (num % 2) == 0:
            if (num % 4) == 0:
                print("Number is even and multiple of 4")
            else:
                print(f'{num} is even number')
        else:
            print(f'{num} is odd number')
        again = False






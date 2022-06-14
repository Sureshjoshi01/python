
n = int(input("Enter a number between 1 and 12 : "))
if n > 12:
    print("Number must be between 1 and 12")
    exit
else:
    for i in range(1,11):
        print(i * n)
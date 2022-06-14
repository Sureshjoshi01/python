compnum = 50
count = 0
str = "y"
while str.upper() == "Y":
    n = int(input("Enter a number : "))
    count = count+1
    if n<50:
        str = input("Too Low, Do you want to guess again(Y/N) ")
    elif n>50:
        str = input("Too High, Do you want to guess again(Y/N) ")
    elif n==50:
        print("Well done, you took", count, "attempts")
        str = "N"
     



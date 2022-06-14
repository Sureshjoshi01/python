str = input("Enter Direction to count(up or down)")
str1 = str.upper()
if str1 == "UP":
    n = int(input("Enter top number tp count upto : "))
    for i in range(1,n+1):
        print(i)
elif str1 == "DOWN":
    n= int(input("Enter a number below 20 : "))
    for i in range(20,n,-1):
        print(i)
else:
    print("I don't underdstand")




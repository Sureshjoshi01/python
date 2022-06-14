n = int(input("Enter number of people invited : "))
if n<=10:
    for i in range(n):
        name = input("Enter name : ")
        print(name,"has benn invited")
elif n>10:
    print("Too many people")
    
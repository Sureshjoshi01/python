#Accept a list of 5 float numbers as an input from the user.

lst = []
for i in range(1,5):
    print("Enter number at location", i, ":")
    n = float(input())
    lst.append(n)


print(lst)
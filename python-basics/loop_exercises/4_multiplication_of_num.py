#Print multiplication table of a given number


def table(n):
    for i in range(1,11):
        print(i * n)


n = int(input("Enter number : "))

print("Table of ",n,":")
table(n)

#Write a Python code to accept a string from the user and display characters present at an even index number.

str = input("Enter a string : ")
l = len(str)
for i in range(l):
    if i % 2 == 0:
        print(str[i])
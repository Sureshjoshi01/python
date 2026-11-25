#Write a program to check if the given file is empty or not

file = open("test.txt","r")
lst = file.readlines()

if len(lst) == 0:
    print("File is Empty")
else:
    print("File is not Empty")
    
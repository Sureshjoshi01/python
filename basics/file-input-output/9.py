import csv 


count = int(input("Enter number of records you want to add : "))
for i in range (0,count):
    file = open("Books.csv","a")
    name = input("Enter Book Name: ")
    author = input("Enter authoe name : ")
    year = input("Enter year : ")
    newrecord = name + "," + author + "," + year + "\n"
    file.write(str(newrecord))
file.close()

file = open("Books.csv","r")
num = 0
search = input("Enter author name :")
for row in file: 
    if search in str(row):
        print(row)
        num = num + 1
if num == 0:
        print("No Books by author")
file.close()


     


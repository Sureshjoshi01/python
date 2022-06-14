import csv 
file = open("Books.csv","a")
name = input("Enter Book Name: ")
author = input("Enter authoe name : ")
year = input("Enter year : ")
newrecord = name + "," + author + "," + year + "\n"
file.write(str(newrecord))
file.close()

file = open("Books.csv","r")
for row in file: 
    print(row)
# Write a Python program to read the text file named “sample.txt” line by line and print each line.

# 1 Method
with open("Tasks_Today.txt","r") as file:
    line = file.readline()
    while line != '':
        print(line,end='')
        line = file.readline()

# 2 Methos
with open("Tasks_Today.txt","r") as file:
    for line in file:
        print(line,end='')

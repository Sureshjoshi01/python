# Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console.


# First method 

f = open("Tasks_Today.txt","r")
print(f.read())
f.close()


# Second Method

with open("Tasks_Today.txt","r") as f:
    print(f.read())


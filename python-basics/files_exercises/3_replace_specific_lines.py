#Write a Python program to read only the first 5 lines of “sample.txt”
try:
    with open("Tasks_Today.txt","r") as f:
        for i in range(5):
            print(f.readline(),end='')
except FileNotFoundError:
    print("ERROR: 'Tasks_Today.txt not found'")

 
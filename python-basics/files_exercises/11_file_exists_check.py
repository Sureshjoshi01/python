# Write a function that takes a filename as input and returns True if the file exists and False otherwise.
import os 

def file_exists(file_name):
    flag = os.path.isfile(file_name)
    if flag:
        print(f"{file_name} is a regular file")
    else:
        print(f"{file_name} does not exists")


file_name ="output1.txt"
file_exists(file_name)
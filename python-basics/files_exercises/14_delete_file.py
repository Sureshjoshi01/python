# Write a program that takes a filename as input and deletes the file. Handle potential errors if the file doesn’t exist.
import os

def delete_file(file_name):
    if not os.path.exists(file_name):
        print(f"{file_name} does not exists")

    try:
        os.remove(file_name)
        print(f"{file_name} was successfully deleted")
    except Exception as e:
        print(e)

file_name = "test3.txt"
delete_file(file_name)

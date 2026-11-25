# Write a program that takes an old filename and a new filename as input and renames the file. Handle potential errors if the old file doesn’t exist.

import os

def rename_file(old_name,new_name):
    try:
        os.rename(old_name,new_name)
        print(f"{old_name} file is successfully renamed to {new_name}")
    except Exception as E:
        print(f"{old_name} file does not exists")

old_name = "test.txt"
new_name = "test1.txt"

rename_file(old_name,new_name)


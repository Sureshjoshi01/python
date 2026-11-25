# Write a function that takes a filename as input and returns the total number of characters in that file (including spaces and newlines).

import os

def count_characters(filename):
    if not os.path.exists(filename):
        print(f"{filename} does not exists")
    
    try:
        with open(filename,'r') as f:
            contents = f.read()

        print(f"Number of characters in {filename}:", len(contents))
    
    except Exception as e:
        print(f"unexpected error",e)

count_characters('test1.txt')
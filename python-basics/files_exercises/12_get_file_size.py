# Write a program to get the size of a file (in bytes).

import os 

file_name = "output.txt"
size = os.path.getsize(file_name)

print(f"Size of file {file_name} is {size} bytes")
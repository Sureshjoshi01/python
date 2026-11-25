# Write a program that reads a text file, replaces all occurrences of a specific word with another word, and writes the modified content to a new file.

import os

def replace_word(input_file,output_file):
    if not os.path.exists(input_file):
        print(f"{input_file} does_not exists")

    try:
        with open(input_file,'r') as file:
            content = file.read()
        modified_content = content.replace("ENG", "EBS")
        with open(output_file,'w') as file:
            file.write(modified_content)
    except Exception as e:
        print(f"Error : {e}")

input_file = "input_file.txt"
output_file = "output_file.txt"

replace_word(input_file,output_file)
        
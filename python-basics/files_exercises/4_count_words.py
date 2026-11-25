# Create a function that takes a filename as input and returns the total number of words in that file.
import os


def count_words(filename):
    if not os.path.exists(filename):
        print(f"{filename} does not exists")

    try:
        with open(filename, 'r') as f:
            contents = f.read()

        words = contents.split(" ")
        print(f"Number of words in {filename}:", len(words))

    except Exception as e:
        print(f"Unexpected Error : ", e)

input_file = "input_file.txt"     
count_words(input_file)
# Write a program to count the occurrences of a specific word (e.g., “hello”) in a given file.

import os

def count_specific_word(filename,word):
    if not os.path.exists(filename):
        print(f"{filename} does not exists")

    try:
        with open(filename) as f:
            contents = f.read().lower()
        
        words = contents.split()
        count = 0
        for i in words:
            if i == word:
                count = count + 1
        print(words)
        print(f"{word} appeas {count} times in {filename}")

    except Exception as e:
        print("unepected error: ", e)

count_specific_word("test1.txt", "done")



        
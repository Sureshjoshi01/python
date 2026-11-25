# Write a code to count the number of unique words in the given a sentence.

sentence = "dog is a simple animal dogs is selfless animal"

lst = sentence.split()

for i in lst:
    i.lower

set1 = set(lst)


print("Number of unique words:", len(set1))
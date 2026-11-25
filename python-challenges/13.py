# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

s = input("Enter a Sequence\n")
l = 0
d = 0
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
for i in s:
    for j in alphabet:
        if i == j:
            l = l + 1
    for j in numbers:
        if i == j:
            d = d + 1
print("LETTERS", l)
print("DIGITS", d) 

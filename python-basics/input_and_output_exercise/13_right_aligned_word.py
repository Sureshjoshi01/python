#Ask the user for a word and a number. 
# Print the word right-aligned in a field of width 20, followed by the number.

wrd = input("Enter a word : ")
number = int(input("Enter a number : "))

print(f"{wrd:>20}{number}")
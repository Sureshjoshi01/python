# Ask the user for a string and print out whether this string is a palindrome or not.

str = input("Enter a string : ")

n = len(str)

rev_str = str[::-1]

if str == rev_str:
    print(str,"is palindrone")
else:
    print(str,"is not palindrone")
print(str)
print(rev_str)
    
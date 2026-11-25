#Reverse a String using Python

def reverse_string(str):
    reverse_string = str[::-1]
    return reverse_string


print("Enter String to be reversed : ",end="")
str = input()

print("Reversed string : ",reverse_string(str))
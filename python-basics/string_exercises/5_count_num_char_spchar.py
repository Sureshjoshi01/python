# Count all letters, digits, and special symbols from a given string
def count_chars(str1):
    num = 0
    char = 0
    spchar = 0
    for i in str1:
        if i.isdigit():
            num = num + 1
        elif i.isalpha():
            char = char + 1
        else:
            spchar = spchar + 1
    return char,num,spchar



str1 = "P@#yn26at^&i5ve"
chars,digits,symbols = count_chars(str1)
print("Total counts of chars, digits, and symbols")
print("chars =",chars)
print("digits =",digits)
print("symbols =",symbols)
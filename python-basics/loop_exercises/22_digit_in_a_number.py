# Write a program in Python identifies the digit with the highest value and the digit with the lowest value within that number.


def find_digit(n):
    if n == 0:
        print("Number is 0 and it has only one digit i.e 0")
        return 0,0
    absolute_value = abs(n)
    st = str(absolute_value)
    highest = int(st[0])  
    lowest = int(st[0])
    for i in st[1:]:
        digit = int(i)
        if digit > highest:
            highest = digit
        if digit < lowest:
            lowest = digit
    return highest, lowest
    
n = int(input("Enter number : "))
highest1, lowest1 = find_digit(n)

print("Largest digit in ",n,":",highest1)
print("Largest digit in ",n,":",lowest1)

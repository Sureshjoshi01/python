# write a function to check number is palindrone or not

def palindrone(number):
    rev = 0
    while number > 0:
        rem = number % 10
        rev = (rev * 10 ) + rem
        number = number // 10 
    return rev

number = int(input("Enter number : "))
rev_number = palindrone(number)
if number == rev_number:
    print(number," is palindrone")
else:
    print(number," is not palindrone")


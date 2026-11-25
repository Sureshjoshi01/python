#Check Palindrome Number

num = int(input("Enter number : "))
original_num = num
rev  = 0
while num >= 1:
    rem  = num % 10
    rev =  (rev * 10) + rem
    num = num // 10


if rev == original_num:
    print("Yes.", original_num, "is Palindrome number.")
else:
    print("No.", original_num, "is not Palindrome number.")


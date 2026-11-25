#Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

n = int(input("Enter the number from which iteration should start :"))
print("Printing current and previous number sum in a range(10)")
for i in range(10):
    
    if i == 0:
        current_number = n
        previous_number = 0
        sum = current_number + previous_number
        print("Current Number",current_number,"Previous Number",previous_number,"Sum:",sum)
        n = n + 1
    else:
        current_number = n
        previous_number = n-1
        sum = current_number + previous_number
        print("Current Number",current_number,"Previous Number",previous_number,"Sum:",sum)
        n = n + 1

#Ask the user for a number. 
# Print this number padded with leading zeros to a width of 5


n = input("Enter a number : ")
padded_number = n.zfill(5)
print(padded_number)
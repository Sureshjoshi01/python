# Question 59

# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example: If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# google

lines = []
while True:
    line = input()
    if line == "":  # Detects the empty line
        break
    lines.append(line)
print(lines)
for i in lines:
    first_name = i.split('@')
    for j in first_name:
        company_name = j.split(".")
    print(company_name[0])

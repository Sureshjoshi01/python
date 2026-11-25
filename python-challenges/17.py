# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based 
# a transaction log from console input. 
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500


lines = []
while True:
    line = input()
    if line == "":  # Detects the empty line
        break
    lines.append(line)
sum = 0
x = []
for i in lines:
    x = i.split(" ")
    if x[0] == "D":
        sum = sum + int(x[1])
    elif x[0] == "W":
        sum = sum - (int(x[1]))     
print(sum)
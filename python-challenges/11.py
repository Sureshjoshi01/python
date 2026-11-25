# Question 11
# Level 2

# Question:
# Write a program which accepts a sequence of comma separated 
# 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001(assuming this type of input from console)
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

num = input()
nums = num.split(",")
print(nums)
for i in nums:
    if int(i) % 5 == 0:
        print(i,end=",")
# Question 60

# Write a program which accepts a sequence of words separated by 
# whitespace as input to print the words composed of digits only.

# Example: If the following words is given as input to the program:

# 2 cats and 3 dogs.

# Then, the output of the program should be:

# ['2', '3']

s = input()
num = ['1','2','3','4','5','6','7','8','9','0']
lst = s.split(" ")
n = []
for i in lst:
    if i in num:
        n.append(i)
print(n)
# Question 65

# Write a program to compute:

# f(n)=f(n-1)+100 when n>0 and f(0)=1

# with a given n input by console (n>0).

# Example: If the following n is given as input to the program:

# 5

# Then, the output of the program should be:

# 500

# In case of input data being supplied to the question, 
# it should be assumed to be a console input.

print("Enter a number : ",end="")
n = int(input())
first = 1

if n == 0:
     print("Enter a number greater than 0")
     exit()
for i in range(1,n+1):
    second = first + 100
    first = second
second = second - 1
print(second)



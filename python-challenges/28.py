# Question 28

# Define a function that can convert a integer into a string and print 
# it in console.

def int_to_str(n):
    str_n = str(n)
    print(type(n))
    print(str_n)
    print(type(str_n))

print("Enter an integer : ",end="")
n = int(input())
int_to_str(n)

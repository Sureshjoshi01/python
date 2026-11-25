# Question 88

# By using list comprehension, please write a program to 
# print the list after removing delete numbers which are 
# divisible by 5 and 7 in [12,24,35,70,88,120,155].

l = [12,24,35,70,88,120,155]
x = [i for i in l if i%5==0 and i%7==0]
print(x)
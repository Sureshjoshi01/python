# Question 45

# Write a program which can filter even numbers in a list by 
# using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

def is_even(num):
    return num % 2 == 0

lst  = [1,2,3,4,5,6,7,8,9,10]

filtered_iterator = filter(is_even, lst)

even_numbers = list(filtered_iterator)
print(even_numbers)
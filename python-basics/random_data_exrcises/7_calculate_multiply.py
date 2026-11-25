# Write a code to calculate multiplication of two random float numbers.

#Note:

#    First random float number must be between 0.1 and 1
#    Second random float number must be between 9.5 and 99.5

import random 

first_number  = random.uniform(0.1,1.0)
second_number = random.uniform(9.5,99.5)

multiplication = first_number * second_number

print("Multiplication of", first_number, "and", second_number, "is : ",multiplication)

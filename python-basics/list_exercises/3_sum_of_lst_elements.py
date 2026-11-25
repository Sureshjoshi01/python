# Calculate and print the sum and average of all numbers in a list.

my_list = [10, 20, 30, 40, 50]

sum = 0
for i in my_list:
    sum = sum + i

avg = sum/len(my_list)

print("Sum:", sum)
print("Average:", avg)

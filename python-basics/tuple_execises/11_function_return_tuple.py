# Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.

def get_min_max(numbers):
    tuple1 = tuple(numbers)
    tuple2 = (min(tuple1), max(tuple1))
    return tuple2

# Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")
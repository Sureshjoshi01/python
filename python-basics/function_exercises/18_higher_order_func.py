# Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, and returns the result of calling func(x, y). Demonstrate its use with different functions (e.g., addition, subtraction).
def apply_operation(func, x, y):
  """
  Applies a given function to two numbers.

  Args:
    func: The function to apply (should take two arguments).
    x: The first number.
    y: The second number.

  Returns:
    The result of calling func(x, y).
  """
  return func(x, y)

# Demonstrate with addition using a regular function
def add(a, b):
  return a + b

result_add = apply_operation(add, 5, 3)
print(f"Result of addition: {result_add}")

# Demonstrate with subtraction using a lambda function
subtract = lambda a, b: a - b
result_subtract = apply_operation(subtract, 10, 4)
print(f"Result of subtraction: {result_subtract}")

# Demonstrate with multiplication using another lambda function
multiply = lambda a, b: a * b
result_multiply = apply_operation(multiply, 2, 6)
print(f"Result of multiplication: {result_multiply}")
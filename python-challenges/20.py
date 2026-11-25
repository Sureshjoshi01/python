# Question 20
# Level 3

# Question:
# Define a class with a generator which can iterate the numbers, 
# which are divisible by 7, between a given range 0 and n.

class DivBy7:

    def __init__(self, n):
        self.n = n

    def generator(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

n = int(input())

obj = DivBy7(n)

for num in obj.generator():
    print(num)
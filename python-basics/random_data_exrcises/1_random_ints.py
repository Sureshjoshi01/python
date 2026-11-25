# Write a code to generate 3 random integers between 100 and 999 which is divisible by 5.

import random

count = 0
while count != 3:
    n = random.randint(100,999)
    if n % 5 == 0:
        print(n)
        count = count + 1

print("\n")
for num in range(3):
    print(random.randrange(100,999,5))


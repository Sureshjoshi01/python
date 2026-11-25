# Write a code to generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
#Note you must adhere to the following conditions:

#    The lottery number must be 10 digits long.
#    All 100 ticket number must be unique.

import random
lottery_tickets = []
for i in range(0,99):
    n = random.randint(1000000000,9999999999)
    lottery_tickets.append(n)

lst2 = random.sample(lottery_tickets,k=2)

print("Lucky Winners are : ")
for i in lst2:
    print(i)   
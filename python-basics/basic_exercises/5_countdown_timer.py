#Write a code to create a simple countdown timer of 5 seconds using a while loop.
import time

num = 5

while num > 0:
    print("Time remaining:", (num) ,"seconds")
    time.sleep(1)
    num = num - 1 

print("Time's up!")
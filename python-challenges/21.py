# Question 21
# Level 3

# Question£º
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. 
# Please write a program to compute the distance from current position 
# after a sequence of 
# movement and original point. 
# If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
import math
x = 0 
y = 0

lst = []

while True:
        s = input()
        if not s:
            break

        direction, steps = s.split(" ")
        steps = int(steps)

        if direction == "UP":
            y=y+steps
        if direction == "DOWN":
            y=y-steps
        if direction == "RIGHT":
            x=x+steps
        if direction =="LEFT":
            x=x-steps

distance = round(math.sqrt(x ** 2 + y ** 2))
print(distance)

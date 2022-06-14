import turtle
import random

random.choice(["red","pink","yellow","green","blue","purple"])
turtle.pensize(3)
for i in range(1,9):
    turtle.color(random.choice(["red","pink","yellow","green","blue","purple"]))
    turtle.forward(100)
    turtle.left(45)


turtle.exitonclick()
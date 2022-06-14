import turtle
import random 

n = random.randint(1,10)


for i in range(1,n):
    len = random.randint(50,100)
    ang =random.randint(0,180)
    turtle.forward(len)
    turtle.right(ang) 

turtle.exitonclick()
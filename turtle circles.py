import turtle
import random

a = turtle.Turtle()
x = random.randint(50,500)
a.speed(0)
a.penup()
a.goto (0, 0-x)
a.pendown
a.pendown()
while x > 10:
    a.circle(x)
    a.penup()
    a.left(90)
    x = x/2
    a.forward(x)
    a.right(90)
    a.pendown()

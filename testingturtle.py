import turtle
import random
import time
from PIL import Image
Width,Height = 1920,1080
screen = turtle.Screen()
screen.setup(Width,Height)
screen.screensize(3*Width, 3*Height)
screen.delay(0)
screen.bgcolor('violet')
turtle.pensize(2)
turtle.pencolor('black')
turtle.tracer(1000,0)
turtle.hideturtle()

def branch(length, decrease, angle, noise=0):


    if length > 10:
        turtle.width(length/7)
        turtle.forward(length)
        new_length=length*decrease
        if noise > 0: 
            new_length *= random.uniform(0.9,1.1)
        angle_l = angle + random.gammavariate(0.3, noise)
        angle_r = angle + random.gammavariate(0.3, noise)

        turtle.left(angle_l)
        branch(new_length,decrease, angle, noise)
        turtle.right(angle_l)

        turtle.right(angle_r)
        branch(new_length,decrease, angle, noise)
        turtle.left(angle_r)

        turtle.backward(length)
    else:
        return

turtle.penup()
turtle.goto(0,-400)
turtle.pendown()
turtle.left(90)
branch(150, 0.8, 25, 10)

img = Image.open("treefrac.eps")
img.save("treefrac.pdf", "PDF")
turtle.tracer()
turtle.Screen().exitonclick()
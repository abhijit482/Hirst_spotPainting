import turtle
import colorgram
from turtle import Turtle, Screen
import random

turtle.colormode(255)
turtle.speed(0)
turtle.bgcolor(161, 112, 131)
dun = Turtle()
dun.setheading(220)
dun.penup() #test koribo hole comment kori dibi
dun.forward(370)
dun.setheading(0)


#color extractor from image
colors = colorgram.extract('spots.png', 30)
rgb = []
for color in colors:
    rgb.append(color.rgb)
saperated_rgb = []
for color_item in rgb:
    a = (color_item.r, color_item.g, color_item.b)
    saperated_rgb.append(a)

def give_colors():
    a = random.choice(saperated_rgb)
    return a

def make_square():
    for _ in range(0, 15):
        for _ in range(0, 15):
            dun.pendown()
            dun.dot(27, give_colors())
            dun.penup()
            dun.forward(35)
        dun.setheading(90)  #north
        dun.forward(35)
        dun.setheading(180)  #west
        dun.forward(525)
        dun.setheading(0) #west


make_square()
screen = Screen()
screen.exitonclick()

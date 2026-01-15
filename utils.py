import random
import colorgram

def draw_shape(turtle,shape):
    if shape=="triangle":
        sides=3
        
    elif shape=="square":
        sides=4
    elif shape=="pentagon":
        sides=5
    elif shape=="hexagon":
        sides=6
    angle=360/sides
    for i in range(0,sides):
        turtle.forward(100)
        turtle.right(angle)


def draw_dash(turtle):
    for i in range(0,7):
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
        turtle.forward(10)

def draw_random(turtle):
    turtle.width(6)
    turtle.speed("fastest")
    for i in range(0,2000):
        turtle.pencolor(random.random(),random.random(),random.random())
        turtle.forward(20)
        angle=random.choice([-360,-270,-180,-90,0,90,270,180,360])
        turtle.right(angle)
    
    
def draw_spyro(turtle):
    turtle.speed("fastest")
    for i in range(0,72):
        turtle.circle(100)
        turtle.right(5)
        turtle.pencolor(random.random(),random.random(),random.random())
    turtle.forward(100)
    draw_spyro(turtle)

def rgb_extractor():
    colors = colorgram.extract('image.jpg', 6)
    first_color=colors[0]
    rgb_first_color=first_color.rgb
    return rgb_first_color,first_color

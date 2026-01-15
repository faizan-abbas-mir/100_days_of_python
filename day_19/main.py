from turtle import Turtle,Screen
from utils import movement

timmy=Turtle()
screen=Screen()
screen.exitonclick()
key=screen.listen()
movement(key,timmy)
screen.onclick() 
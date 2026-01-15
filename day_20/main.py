from turtle import Turtle, Screen
from snake import Snake
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.title("Snake game")
screen.tracer(0)

snake=Snake()

    
game_ison=True

while game_ison:
    screen.update()
    time.sleep(0.1)
    snake.move()
        
    
        
          
        



screen.exitonclick()
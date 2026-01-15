from turtle import Turtle


position=[(0,0),(-20,0),(-40,0)]
segements=[]
DISTANCE=23

class  Snake:
    def __init__(self):
        self.segements=[]
        self.create_snake()


    def create_snake(self):    
        for positions in position:
            new_segement=Turtle(shape="square")
            new_segement.penup()
            new_segement.goto(positions)
            self.segements.append(new_segement)
       

    def move(self):
        for segment_num in range(len(self.segements)-1,0,-1):
            new_x=self.segements[segment_num-1].xcor()
            new_y=self.segements[segment_num-1].ycor()
            self.segements[segment_num].goto(new_x,new_y)
        self.segements[0].forward(DISTANCE)


from turtle import Turtle,Screen
#Create the Snake Body and Class, starting with 3 white squares.
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
#make segments list and snake object for snake body, that will get appended with each new body part
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    #initialize self and classmethods
    def __init__(self):
        #segments of the snake list start at 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    #create snake classmethod
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    #add snake parts when get food
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
        
    #reset when snake dies, reset new body
    def reset(self):
        #for loop to clear old snake Body
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
        #do extend when added    
    def extend(self):
        self.add_segment(self.segments[-1].position())
        #move in accordance to x and y coordinates
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)
        #arrow keys
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

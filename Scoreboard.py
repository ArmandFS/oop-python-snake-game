#Scoreboard Class
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,370)
        self.hideturtle()
        self.update_scoreboard()
        #update the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align =ALIGNMENT ,font = FONT)
       #game over text if fail game
        
            
    def reset(self):
       #if the score is > high score then that score becomes the new high score
       if self.score > self.high_score:
           self.high_score = self.score
           with open("snake_data.txt", mode ="w") as data:
               data.write(f"{self.high_score}")
       self.score = 0
       self.update_scoreboard()
       
       
      #increase score function
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
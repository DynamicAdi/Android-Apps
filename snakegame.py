#pylint:disable=W0143
#pylint:disable=W0311

import turtle 
import time
import random

delay = 0.1 

# Scores 
score = 0 
high_score = 0 

# SCREEN 

wn = turtle.Screen()
wn.title("SNAKE GAME by DEV. Lover")
wn.bgcolor("white")
wn.setup(width=300, height=300)
wn.tracer(0)

# SNAKE HEAD 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# FOOD

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)


segments = []

# Scores 
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("red")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0 High Score: 0", align = "center",font=("calibri",14, "bold"))

# FUNCS 
def go_up():
    if head.direction != "down": #fix here
       head.direction = "up"
      
   
def go_down():
    if head.direction != "up":
       head.direction = "down"
     
    
def go_left():
    if head.direction != "right":
       head.direction = "left"
      
   
def go_right():
    if head.direction != "left":
       head.direction = "right"
     
   
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
     
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
        
# KEYS ON KEYBOARD

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#Mainloop
while True:
    wn.update()
    
    
# BORDERS 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(2) # fix here
        head.direction = "stop"
        
        # HIDE THE segments 
        for segment in segments:
            segment.goto(1000,1000) # out of range
        segments.clear()
        
# SCORE == 0 again 
        score = 0 
        
        delay = 0.1 
        
        sc.clear()
        sc.write("score: {} High Score: {}".format(score, high_score), align = "center",font=("calibri",14, "bold"))
        
# CHECK COLLISION with food 
    if head.distance(food) <20:
       # FOOD MOVES RANDOMLY 
       x = random.randint(-290,290)
       y = random.randint(-290,290)
       food.goto(x,y)
     
   
# NEW SEGMENT FOR HEAD 
       new_s = turtle.Turtle()
       new_s.speed(0)
       new_s.shape("square")
       new_s.color("black")
       new_s.penup()
       segments.append(new_s)
       
       # Short the delay 
       delay -= 0.001
       # INCREASE OF SCORE 
       score += 5
       
       if score > high_score:
           high_score = score 
       sc.clear()
       sc.write("score: {} High Score: {}".format(score, high_score), align = "center",font=("calibri",14, "bold"))
       
# MOVEMENT 

for index in range(len(segments)-1,0,-1):
    x = segments[index-1].xcor()
    y = segments[index -1].ycor()
    segments[index].goto(x,y)
    
# INCREASE in length 
if len(segments)>0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)
  
move()

# COLLISION with body 
for segment in segments:
    if segement.distance(head)<20:
       time.sleep(1)
       head.goto(0,0)
       head.direction = "stop"
       
       # HIDE LF SNAKE 
       for segement in segments:
           segement.goto(1000,1000)
       segments.clear()
       score = 0 
       delay = 0.1
       
       # SCORE +VE 
       sc.clear()
       sc.write("score: {} High Score: {}".format(score, high_score), align = "center",font=("calibri",14, "bold"))
time.sleep(delay)
wn.mainloop()


# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random 

#-----game configuration----
shape = "turtle"
size = 5
color = "blue"
score = 0

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
bob = trtl.Turtle(shape = shape)
bob.color(color)
bob.shapesize(size)
bob.speed(0)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-370, 270)
score_writer.hideturtle()

font = ("Arial", 30, "bold")
score_writer.write(score, font=font)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(275, 275)

#-----game functions--------
def turtle_clicked(x,y):
    print("bob was clicked")
    change_position()
    score_counter()

def change_position():
    bob.penup()
    bob.ht()
    if not timer_up:
      new_xpos = random.randint(-400, 400)
      new_ypos = random.randint(-300, 300)
      bob.goto(new_xpos, new_ypos)
      bob.st()

def score_counter():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Game Over", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


#-----events----------------
bob.onclick(turtle_clicked)

wn = trtl.Screen()
wn.bgcolor("red")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()

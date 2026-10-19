from turtle import Turtle,Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colour(red,blue,yellow,green,purple,black): ")
print(user_bet)
speed = [10,12,14,16,18,20]
a = Turtle(shape = "turtle")
a.color("red")
a.speed(random.choice(speed))
a.penup()
a.goto(-230, 150)
b = Turtle(shape = "turtle")
b.color("blue")
b.speed(random.choice(speed))
b.penup()
b.goto(-230, 90)
c = Turtle(shape = "turtle")
c.color("yellow")
c.speed(random.choice(speed))
c.penup()
c.goto(-230, -30)
d = Turtle(shape = "turtle")
d.color("green")
d.speed(random.choice(speed))
d.penup()
d.goto(-230, -60)
e = Turtle(shape = "turtle")
e.color("black")
e.speed(random.choice(speed))
e.penup()
e.goto(-230, -90)
f = Turtle(shape = "turtle")
f.color("purple")
f.speed(random.choice(speed))
f.penup()
f.goto(-230, -150)
while True:
    a.forward(random.randint(1,10))
    b.forward(random.randint(1,10))
    c.forward(random.randint(1,10))
    d.forward(random.randint(1,10))
    e.forward(random.randint(1,10))
    f.forward(random.randint(1,10))
    if a.xcor() >= 230:
        winner = "red"
        break
    if b.xcor() >= 230:
        winner = "blue"
        break
    if c.xcor() >= 230:
        winner = "green"
        break
    if d.xcor() >= 230:
        winner = "yellow"
        break
    if e.xcor() >= 230:
        winner = "purple"
        break
print("The winner is: ",winner)
if user_bet.lower() == winner:
    print("You won the bet")
else:
    print("You lost the bet")
screen.exitonclick()
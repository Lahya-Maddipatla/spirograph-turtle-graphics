from turtle import *
import random
t=Turtle()
colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t.color(random_color())
        t.speed("fastest")
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)
draw_spirograph(5)  
s=Screen()
s.exitonclick()
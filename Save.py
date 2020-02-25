from turtle import *
from random import *
color("darkgreen")
shape("turtle")
colors=["blue","black","green","yellow","red","violet"]

for i in range(400):
    print("!")
    left(randint(-90,90))
    color(colors[randint(0,5)])
    circle(100,randint(-180,180))
    print("!")

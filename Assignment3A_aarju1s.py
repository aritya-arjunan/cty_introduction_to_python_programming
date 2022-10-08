# Make sure that the map.gif file is in the same place
# on your computer as this one!

import turtle

turtle.Screen().setup(1093, 440)
turtle.Screen().bgpic("map.gif")

# Type your code here.
t = turtle.Pen()
forward = 60
forward2 = 30
forward3 = 90
angle = 120
t.penup()
t.right(90)
t.forward(95)
t.right(90)
t.forward(110)
t.pendown()
t.forward(forward)
t.right(angle)
t.forward(forward)
t.right(angle)
t.forward(forward)
t.penup()

t.left(150)
t.forward(242)
t.left(90)
t.forward(55)
t.pendown()
t.forward(forward2)
t.right(angle)
t.forward(forward2)
t.right(angle)
t.forward(forward2)
t.right(angle)
t.penup()

t.backward(320)
t.left(90)
t.forward(290)
t.right(90)
t.pendown()
t.forward(forward3)
t.right(angle)
t.forward(forward3)
t.right(angle)
t.forward(forward3)

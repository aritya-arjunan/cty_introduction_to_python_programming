# Make sure that the map.gif file is in the same place
# on your computer as this one!

import turtle

turtle.Screen().setup(1093, 440)
turtle.Screen().bgpic("map.gif")

# Type your code here.
t = turtle.Pen()
forward1 = 30
forward2 = 60
angle = 120
t.penup()
t.right(90)
t.forward(95)
t.right(90)
t.forward(140)
t.pendown()
t.forward(forward1)
t.right(angle)
t.forward(forward2)
t.right(angle)
t.forward(forward2)
t.right(angle)
t.forward(forward1)

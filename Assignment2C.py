# Make sure that the map.gif file is in the same place
# on your computer as this one!

import turtle

turtle.Screen().setup(1093, 440)
turtle.Screen().bgpic("map.gif")

# Type your code here.
t = turtle.Pen()
t.penup()
t.right(90)
t.forward(120)
t.right(90)
t.forward(240)
t.pendown()
t.circle(5)
t.penup()
t.forward(15)
t.right(90)
t.forward(15)
t.pendown()
t.circle(5)

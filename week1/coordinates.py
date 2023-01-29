"""
Name: coordinates.py

Description:

Write the coordinates of the canvas.

Author:

Date:

Here is a list of colours: https://trinket.io/docs/colors, click on the 
colour to see the turtle name
"""
from turtle import *

# write some coordinates on the canvas
penup()
goto(0,0)
pendown()
write("(0,0)")
penup()
goto(300,0)
pendown()
write("(300,0)")
penup()
goto(-300,0)
pendown()
write("(-300,0)")
penup()
goto(0,300)
pendown()
write("(0,300)")
penup()
goto(0,-300)
pendown()
write("(0,-300)")
penup()
goto(0,0)
pendown()

# DO NOT DELETE THIS LINE
# leave the turtle on the screen until the user clicks in the screen
exitonclick()

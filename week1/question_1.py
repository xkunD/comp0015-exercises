"""
Name: question_1.py

Description:

Draw a square.

Author:

Date:

Here is a list of colours: https://trinket.io/docs/colors, click on the 
colour to see the turtle name
"""
from turtle import *

# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)   # same as goto(-300,0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("pale violet red")

# Draw a square
forward(50)     # move forward 50 pixels
left(90)        # turn left 90 degrees
forward(50)
lt(90)          # an abbreviation for turn left
fd(50)          # an abbreviation for move forward
lt(90)
fd(50)
lt(90)

penup()
goto(-220, 0)
pendown()

pencolor("coral")

fd(80)
lt(90)
fd(80)
lt(90)
fd(80)
lt(90)
fd(80)
lt(90)

penup()
fd(120)
pendown()

pencolor("olive drab")

fd(100)
lt(90)
fd(100)
lt(90)
fd(100)
lt(90)
fd(100)
lt(90)




penup()
fd(150)
pendown()

pencolor("dodger blue")

fd(130)
lt(90)
fd(130)
lt(90)
fd(130)
lt(90)
fd(130)
lt(90)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
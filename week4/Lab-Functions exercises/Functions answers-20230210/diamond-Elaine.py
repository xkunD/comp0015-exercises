"""
    This program prompts the user for the height of a diamond and prints it.

    Author: Elaine Pimentel
    The problem was created by Rob Miller, DIS, UCL for a Java course.
    Date: January 2023
"""

MARGIN = 10
# Draw the triangle
def triangle(symbol, t_height) :
    for line_number in range(1,t_height+1) :
        print(" " * (MARGIN + t_height - line_number), symbol * (line_number * 2 - 1))

# Draw the reverse triangle
def reverse_triangle(symbol, rt_height) :
    for line_number in range(rt_height - 1,0,-1) :
        print(" " * (MARGIN + rt_height - line_number), symbol * (line_number * 2 - 1))

# Glue the two together
def diamond(symbol, height) :
    half_height = height // 2 + 1 # Remember that the diamond is split in two parts
    triangle(symbol, half_height)
    reverse_triangle(symbol,half_height)

def main() :
    height = int(input("\n\tEnter the number of lines for the diamond: "))
    brick_character = input("\tEnter the character from which the diamond should be made: ")
    if height % 2 != 1: # Handle the even case
        height += 1
    diamond(brick_character,height)


# Start the program
if __name__ == "__main__":
    main()

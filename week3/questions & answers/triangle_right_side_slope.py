"""
Name: triangle_right_side_slope.py
Description: This program prompts the user to enter the height of the triangle and prints a
right-angled triangle with the slope on the right.

Author: Rae Harbird

Date: August 2018
"""

MARGIN = 10


def main():
    
    height = int(input("\n\tEnter the height of the triangle: "))
    
    print("\n\n")
    for i in range(1, height + 1):
        print(" " * MARGIN, "*" * i)


if __name__ == "__main__":
    main()

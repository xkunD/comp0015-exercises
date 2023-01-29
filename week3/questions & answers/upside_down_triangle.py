"""
Name: upside_down_triangle.py
Description: This program prompts the user to enter the height of the triangle and prints a
right-angled triangle with the slope on the right.

Author: Rae Harbird

Date: August 2018
"""

MARGIN = 10


def main():
    
    height = int(input("\n\tEnter the height of the triangle: "))
    print()

    for num_stars in range(height, 0, -1):
         print(" " * MARGIN, "*" * num_stars)


if __name__ == "__main__":
    main()

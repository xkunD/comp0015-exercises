"""
Name: pyramid.py
Description: This program prompts the user to enter the height of the pyramid and prints a
pyramid.

Author: Rae Harbird

Date: August 2018
"""

MARGIN = 10
SYMBOL = "*"


def main():
    
    height = int(input("\n\tEnter the height of the pyramid: "))
    
    print("\n\n")


    for num_spaces in range(height - 1, -1, -1):
        print(" " * MARGIN, " " * num_spaces, end="")
        num_symbols = (height - num_spaces) * 2 - 1
        print(SYMBOL * num_symbols)


if __name__ == "__main__":
    main()

"""
Name: quiz2.py
Description:

This program returns the largest two numbers from a serie of integers given by the user.
We assume that the user will enter at least two integers before typing 0.

Author: Elaine Pimentel

Date: January 2023
"""


def main():
    n1 = int(input("Enter an integer: "))
    n2 = int(input("Enter an integer: "))
    large1 = max(n1,n2)
    large2 = min(n1,n2)
    n = 99
    while n != 0 :
        n = int(input("Enter an integer: "))
        if n > large1 :
            large2 = large1
            large1 = n
        elif n > large2 :
            large2 = n
    print(f'The largest two numbers are {large1}, {large2}')



if __name__ == "__main__":
    main()

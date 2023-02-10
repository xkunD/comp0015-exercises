# Name: guess_two_randoms_simplified.py
# Description: This program asks the user to guess two numbers.
#
# Author: Rae Harbird
# Date: August 2018

import random

MIN = 1
MAX = 5


def main():
    
    first_answer = random.randint(MIN, MAX)
    second_answer = random.randint(MIN, MAX)
    
    first_guess = int(input("\n\tGuess the first number between " + str(MIN) + " and " + str(MAX) + ": "))
    second_guess = int(input("\n\tGuess the second number between " + str(MIN) + " and " + str(MAX) + ": "))

    if first_guess == first_answer and second_guess == second_answer:
        print("\tCorrect - well done!")
    else:
        print("\tNo, the answers were ", end='')
        print(str(first_answer) + " and " + str(second_answer) + ".\n")


if __name__ == "__main__":
    main()

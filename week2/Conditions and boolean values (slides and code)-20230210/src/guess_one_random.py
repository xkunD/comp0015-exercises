# Name: guess_one_random.py
# Description: This program asks the user to guess a number.
#
# Author: Rae Harbird
# Date: August 2018

import random

MIN = 1
MAX = 5


def main():

    answer = random.randint(MIN, MAX)

    guess = int(input("\n\tGuess the number between " + str(MIN) + " and "
                      + str(MAX) + ": "))
    if guess == answer:
        print("\tCorrect - well done!")
    if guess != answer:
        print("\tNo, the answer was " + str(answer) + ".\n")


if __name__ == "__main__" :
    main()


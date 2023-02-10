# Name: generate_random.py
# Description: This program generates a random number.
#
# Author: Rae Harbird
#
# Date: August 2018
#

import random

MIN = 1
MAX = 5


def main():

    random_number = random.randint(MIN, MAX)
    print("A random number between " + str(MIN), end="")
    print(" and " + str(MAX) + ": " + str(random_number))


if __name__ == "__main__" :
    main()

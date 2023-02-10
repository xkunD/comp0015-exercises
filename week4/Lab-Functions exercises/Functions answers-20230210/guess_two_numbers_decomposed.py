"""
Name: guess_two_numbers_decomposed.py

Description:

This program prompts the user for two numbers and checks whether they match two
randomly generated numbers.

Author: Rae Harbird
This problem was created by Rob Miller, DIS, UCL for a Java course.

Date: August 2018
"""

import random

MIN = 1
MAX = 3


def output_yes():
    print("\tCorrect - well done!\n")

def output_no(answer_a, answer_b):
    """
    Checks the two guesses entered by the user against the two randomly generated numbers.
    @params answer_a the first answer
    @params answer_b the second answer
    """

    print("\tNo, the answers were {} and {}.\n".format(answer_a, answer_b))

def guesses_ok(answer_a, answer_b, guess_a, guess_b):
    """ 
    Checks the two guesses entered by the user against the two randomly generated numbers.
    @params answer_a the first answer
    @params answer_b the second answer
    @params guessA the first guess
    @params guessB the second guess
    @return True or False
    """

    ok_same_order = guess_a == answer_a and guess_b == answer_b
    ok_other_order = guess_a == answer_b and guess_b == answer_a
    return ok_same_order or ok_other_order


def main():

    
    first_answer = random.randrange(MIN, MAX + 1)
    second_answer = random.randrange(MIN, MAX + 1)
    
    first_guess = int(input("\n\tGuess the first number between {} and {}: "\
                            .format(MIN, MAX)))
    second_guess = int(input("\n\tGuess the second number between {} and {}: "\
                             .format(MIN, MAX)))

    if guesses_ok(first_answer, second_answer, first_guess, second_guess):
        output_yes()
    else:
        output_no(first_answer, second_answer)


# Start the program
if __name__ == "__main__":
    main()

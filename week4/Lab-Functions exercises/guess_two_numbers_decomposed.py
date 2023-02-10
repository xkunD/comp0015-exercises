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

"""
Checks the two guesses entered by the user against the two randomly generated numbers.
@params answerA the first answer
@params answerB the second answer
@params guessA the first guess
@params guessB the second guess
@return True or False
"""


def guesses_ok(answer_a, answer_b, guess_a, guess_b):
    ok_same_order = guess_a == answer_a and guess_b == answer_b
    ok_other_order = guess_a == answer_b and guess_b == answer_a
    return ok_same_order or ok_other_order

def output_yes():
    print("\tCorrect - well done!\n")

def output_no(first_answer, second_answer):
    print(f"\tNo, the answers were {first_answer} and {second_answer}.\n")

def main():
    min = 1
    max = 3
    
    first_answer = random.randrange(min, max + 1)
    second_answer = random.randrange(min, max + 1)
    
    first_guess = int(input(f"\n\tGuess the first number between {min} and {max}: "))
    second_guess = int(input(f"\n\tGuess the second number between {min} and {max}: "))

    if guesses_ok(first_answer, second_answer, first_guess, second_guess):
        output_yes()
    else:
        output_no(first_answer, second_answer)


# Start the program
if __name__ == "__main__":
    main()

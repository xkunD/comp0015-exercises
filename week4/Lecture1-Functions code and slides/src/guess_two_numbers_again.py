# Name: guess_two_numbers_again.py
#
# Description:
#
# This program prompts the user for two numbers and checks whether they
# match two randomly generated numbers.
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#
import random

MIN = 1
MAX = 3

def guessesOk(answerA, answerB, guessA, guessB):
    '''
    Test whether answers are the same as guesses.
    
    Parameters
    ----------
    answerA : int
        First number
    answerB : int
        Second number
    guessA : int
        Answer chosen by the user
    guessB : int
        The other answer chosen by the user

    Returns
    -------
    bool
        Result of testing whether answers are the same as guesses
    '''
    okSameOrder =  guessA == answerA and guessB == answerB
    okOtherOrder = guessA == answerB and guessB == answerA
    return okSameOrder or okOtherOrder
    

def main() :
    
    firstAnswer = random.randrange(MIN, MAX + 1)
    secondAnswer = random.randrange(MIN, MAX + 1)
    
    firstGuess = int(
        input(f"\n\tGuess the first number between {MIN} and {MAX}: "))
    secondGuess = int(
        input(f"\n\tGuess the second number between {MIN} and {MAX}: "))

    if guessesOk(firstAnswer, secondAnswer, firstGuess, secondGuess):
        print("\tCorrect - well done!\n")
    else:
        print(f"\tNo, the answers were {firstAnswer} and {secondAnswer}.\n")


# Start the program
if __name__ == "__main__":
    main()

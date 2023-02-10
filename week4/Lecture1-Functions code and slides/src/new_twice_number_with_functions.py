# This program prompts the user to type in a number and prints the number
# and double the number.
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#


def twice_number(the_number) :
    '''Return twice the number.'''
    the_number = the_number * 2
    return the_number


def main():
    the_number = int(input("Enter a value for 'number': "))
    print(f"The value of 'number' is {the_number}.")
    new_number = twice_number(the_number)
    print(f"The value of 'twice_number' is: {new_number}.")


if __name__ == "__main__":
    main()

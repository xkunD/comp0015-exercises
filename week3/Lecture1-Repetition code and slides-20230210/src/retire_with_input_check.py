# Name: retire_with_input_check.py
#
# Description:
#
# This program prompts the user for their age calculates the year in which they 
# can retire.
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#


RETIREMENT_AGE = 70
MAX_AGE = 130


def main():
    
    users_age = int(input("\nEnter your age: "))

    while users_age < 0 or users_age > MAX_AGE:
        print("\tDon't be stupid! Enter your real age: ")
        users_age = int(input("\nEnter your age: "))
    
    if users_age < RETIREMENT_AGE:
        print("You will retire in ", end="")
        print(RETIREMENT_AGE - users_age," years.\n")
    elif users_age == RETIREMENT_AGE:
        print("You will retire this year.")
    elif users_age > RETIREMENT_AGE:
        print("You retired ", end="")
        if users_age - RETIREMENT_AGE == 1:
            print(users_age - RETIREMENT_AGE," year ago.\n")
        else:
            print(users_age - RETIREMENT_AGE," years ago.\n")


if __name__ == "__main__":
    main()

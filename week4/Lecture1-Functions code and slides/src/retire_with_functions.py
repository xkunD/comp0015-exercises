# Name: retire_with_functions.py
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
MAX_VALID_AGE = 130



def get_age():
    '''Checks the age entered by the user and returns a valid age.'''
    age_not_valid = True
    
    while age_not_valid :
        age = int(input("Enter your age: "))        
        if age < 0 or age > MAX_VALID_AGE :
            print("\tDon't be stupid! Enter your real age: ")
        else :
            age_not_valid = False

    return age


def main():
    users_age = get_age()
    
    if users_age < RETIREMENT_AGE :
        print("You will retire in ", end="")
        print(RETIREMENT_AGE - users_age," years.\n")
    elif users_age == RETIREMENT_AGE :
        print("You will retire this year.")
    elif users_age > RETIREMENT_AGE :
        print("You retired ", end="")
        if users_age - RETIREMENT_AGE == 1 :
            print(users_age - RETIREMENT_AGE," year ago.\n")
        else :
            print(users_age - RETIREMENT_AGE," years ago.\n")


# Start the program
if __name__ == "__main__":
    main()

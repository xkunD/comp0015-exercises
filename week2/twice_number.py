# Name: twice_number.py
# Description:
#
# This program prompts the user to type in a number and prints the number and double the number. 
#


def main():
    number = int(input("Enter a value for 'number': "))
    double_number = number * 2
    print(f'The value of \'number\' is {number:2d} \n The number of \'twice number\' is {double_number:2d}.')

if __name__ == "__main__":
    main()
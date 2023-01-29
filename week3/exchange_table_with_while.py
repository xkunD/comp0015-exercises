# Name: exchange_table_with_while.py
#
# Description:
#
# This program prints an exchange table after prompting for a starting value
# and the number of lines that the table should have.
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#

EXCHANGE_RATE = 1.564


def main():
    uk_amount = float(input("\nEnter a starting amount in UK sterling: "))
    number_of_lines = int(input("\nEnter the number of lines for the table: "))

    print("\n\tPOUNDS\t\tEUROS")
    
    line_counter = 1
    
    while line_counter <= number_of_lines:
        print("\t{:.2f}\t\t{:.2f}".format(uk_amount, uk_amount * EXCHANGE_RATE))
        uk_amount = uk_amount + 10
        line_counter += 1


if __name__ == "__main__":
    main()

# Name: exchange_table_with_while.py
#
# Description:
#
# This program prints an exchange table after prompting for a starting value
# and the number of lines that the table should have.
#
# Author: Rae Harbird
#
# Date: August 2018
#


def main():

    EXCHANGE_RATE = 1.564

    again = 'y'

    while again == 'y':
        uk_amount = float(input("\nEnter a starting amount in UK sterling: "))
        number_of_lines = int(input("\nEnter the number of lines for the table: "))

        print("\n\tPOUNDS\t\tEUROS")

        for line_counter in range(number_of_lines):
            print("\t{:.2f}\t\t{:.2f}".format(uk_amount,
                                    uk_amount * EXCHANGE_RATE))
            uk_amount = uk_amount + 10

        again = input("go again? (y/n)? ")


if __name__ == "__main__":
    main()

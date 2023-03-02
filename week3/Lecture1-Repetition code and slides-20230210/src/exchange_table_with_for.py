# Name: exchange_table_with_for.py
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
    NUM_LINES = 10 
    EXCHANGE_RATE = 1.564

    print("\n\tPOUNDS\t\tEUROS")
    uk_amount = 1

    for line_counter in range(NUM_LINES):
        print("\t{:.2f}\t\t{:.2f}".format(uk_amount, uk_amount * EXCHANGE_RATE))
        uk_amount = uk_amount + 10


if __name__ == "__main__":
    main()

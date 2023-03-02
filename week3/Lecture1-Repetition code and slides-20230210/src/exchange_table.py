# Name: exchange_table.py
#
# Description:
#
# This program prints an exchange table after prompting for a starting value. 
#
# Author: Rae Harbird
#
# Date: August 2018
#

EXCHANGE_RATE = 1.564


def main():
    uk_amount = float(input("\nEnter a starting amount in UK sterling: "))
    print("\n\tPOUNDS\t\tEUROS")
    print(f"\t{uk_amount:.2f}\t\t{uk_amount:.2f}")
    uk_amount = uk_amount + 10
    print("\t{:.2f}\t\t{:.2f}".format(uk_amount, uk_amount * EXCHANGE_RATE))
    uk_amount = uk_amount + 10
    print("\t{:.2f}\t\t{:.2f}".format(uk_amount, uk_amount * EXCHANGE_RATE))
    
    
if __name__ == "__main__":
    main()

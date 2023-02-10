"""
Name: quiz1.py
Description:

This program calculates the total amount to pay the TA.


Author: Elaine Pimentel

Date: January 2023
"""


def main():
    rate_pay = float(input("Enter the hourly rate of pay: "))
    hours_worked = int(input("Enter the number of hours worked: "))
    if hours_worked <= 8 :
        total_pay = rate_pay * hours_worked
    else :
        total_pay = rate_pay * 8 + rate_pay * (hours_worked - 8) * 1.5
    print(f'The total amount to pay the TA is {total_pay:.2f}')



if __name__ == "__main__":
    main()

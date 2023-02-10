"""
Name: question_3.py
Description:

This program calculates how old someone will be in a given year,
after prompting for the current year and user's age.


Author: Rae Harbird
This problem was created by Rob Miller, DIS, UCL for a Java course.

Date: August 2018
"""


def main():
    year_now = int(input("Enter the current year then press RETURN: "))
    month_now = int(input("Enter the current month (a number from 1 to 12): "))
    age_now = int(input("Enter your current age in years: "))
    month_born = int(input("Enter the month in which you were born (a number from 1 to 12): "))
    another_year = int(input("Enter the year in which you wish to know your age: "))
    another_month = int(input("Enter the month in this year: "))

    # Convert everything to months and then do the same calculation

    if month_now < month_born:
        months_since_birthday = 12 + month_now - month_born
    else:
        months_since_birthday = month_now - month_born

    age_now_in_months = age_now * 12 + months_since_birthday

    another_year_in_months = another_year * 12 + another_month

    another_age_in_months = another_year_in_months - ((year_now * 12 + month_now) - age_now_in_months)

    if another_age_in_months < age_now_in_months:
        print("The year and month for which you wish to know your age can't be in the past.")

    if another_age_in_months < 0:
        print(f"You weren't born in {another_year_in_months - age_now_in_months}.")

    if another_age_in_months > 150 * 12:
        print(f"Sorry, but you'll probably be dead by month {another_month}, {another_year}!")

    if 150 * 12 > another_age_in_months >= age_now_in_months:
        if another_age_in_months % 12 == 1:
            print(f"Your age in {another_month}/{another_year} will be {int(another_age_in_months / 12)}\
                    years and {another_age_in_months % 12} month")                                                                           ,
        else:
            print(f"Your age in {another_month}/{another_year} will be {int(another_age_in_months / 12)}\
                    years and {another_age_in_months % 12} months")                                                                           ,


if __name__ == "__main__":
    main()

# Elaine: you may also calculate the year of birth and follow from that!
"""
Name: leap_year_table.py
Description: This program prompts the user to enter a start year and
end year prints a table of leap years in the range.

Author: Rae Harbird

Date: August 2018
"""

ROW_LENGTH = 6

def main():

 

    start_year = int(input("Enter the start year for the range: "))

    # Assume end of range is inclusive
    end_year = int(input("Enter the end year for the range: "))

    # leapString -  a string containing all the leap years, formatted nicely
    leap_string = ""

    # rowCounter - Keep track of where we are in the row.
    column = 1

    # leap - flag used to check whether a year is a leap year
    leap = False

    # leapYear - the current leap year
    # leap_year = 0

    # Go through the range once to find the last leap year in the range.
    last_leap_year = 0
    for year in range(start_year, end_year + 1):
        if year % 400 == 0:
            last_leap_year = year
        elif year % 4 == 0 and year % 100 != 0:
            last_leap_year = year
    

    for year in range(start_year, end_year + 1):

        if year % 400 == 0:
            leap = True
            leap_year = year
        elif year % 4 == 0 and year % 100 != 0:
            leap = True
            leap_year = year
        else:
            leap = False

        # Deal with print formatting

        if leap:
            if leap_year == last_leap_year:
                leap_string = leap_string + str(leap_year) + "."
            elif column == ROW_LENGTH:
                leap_string = leap_string + str(leap_year) + ", " + "\n"
                column = 1
            else:
                leap_string = leap_string + str(leap_year) + ", "
                column = column + 1


    print(f"\n Leap years in range {start_year}-{end_year}\n")
    print(leap_string)


if __name__ == "__main__":
    main()

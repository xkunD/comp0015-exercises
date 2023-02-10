"""
    This program prompts the user for two numbers and prints a square of digits in which the columns increase by 1 and
    the rows also increase by one.

    This problem is from “Building Python Programs” by: Stuart Reges, Marty Stepp, and Allison Obourn, 2018.
    Date: August 2018
"""

MARGIN = " " * 10


def number_square(start, end):
    """
    Construct the string representing the square

    Parameters
    ----------
    start : int
        the start of the range

    end : int
        the end of the range

    Returns
    -------
    str
        the string representing the square

    """
    square_string = ""
    for current_line in range(start, end + 1):
        square_string += square_line(current_line, start, end)
    return square_string


def square_line(current_number, start_range, end_range):
    """
    Construct the string representing a line of the square

    Parameters
    ----------
    current_number : int
        the number that starts this line of the square

    start_range : int
        the start of the range

    end_range : int
        the end of the range

    Returns
    -------
    str
        the string representing the line

    """
    line_string = MARGIN + str(current_number)
    for i in range(end_range - start_range):
        current_number += 1
        if current_number > end_range:
            current_number = start_range
        line_string += str(current_number)
    line_string += "\n"
    return line_string


def main():
    start_num = int(input("\n\tEnter the start number: "))
    end_num = int(input("\tEnter the end number: "))
    if start_num < end_num:
        print(number_square(start_num, end_num))
    else:
        print(number_square(end_num, start_num))


# Start the program
if __name__ == "__main__":
    main()

"""
Name: pyramid.py

Description:

This program prompts the user for the height of a pyramid and prints it.

Author: Rae Harbird
This problem was created by Rob Miller, DIS, UCL for a Java course.

Date: August 2018
"""

MARGIN = 10

def pyramid_line(symbol, line_number, height):
    """ Construct string representing a line of the pyramid

    Parameters
    ----------
    line_number : int
        Line number of the current line
    symbol : str
        Symbol from which the pyramid will be printed
    height : int
        Height of the pyramid

    Returns
    -------
    str
        The string representing a line of the pyramid
    """
    
    line = ""
    line += spaces_for_pyramid_line(line_number, height)
    line += symbols_for_pyramid_line(symbol, line_number)
    line += "\n"
    return line


def symbols_for_pyramid_line(symbol, line_num):
    """
    Construct string representing the symbols for a line of the pyramid
    
    Parameters
    ----------
    line_num : int
        Line number of the current line
    symbol : str
        Symbol from which the pyramid will be printed

    Returns
    -------
    str
        The string representing the symbols for a line of the pyramid
    """
    
    line_symbols = ""
    line_symbols += symbol * ((line_num * 2) - 1)
    return line_symbols


def spaces_for_pyramid_line(line_num, height):
    """
    Construct and return string representing spaces for a line of the pyramid.
    
    Parameters
    ----------
    line_num : int
        Line number of the current line
    height : int
        Height of the pyramid

    Returns
    -------
    str
        The string representing the spaces for pyramid
    """
    
    line_spaces = ""
    line_spaces += " " * (MARGIN + height + 1 - line_num)
    return line_spaces


def pyramid_string(character, height):
    """
    Construct and return the string representing the pyramid
    
    Parameters
    ----------
    character : str
        Character the symbol from which the pyramid will be printed
    height : int
        Height the height of the pyramid

    Returns
    -------
    str
        The string representing the pyramid
    """
    
    pattern = "\n"
    for line_count in range(1, height + 1):
        pattern += pyramid_line(character, line_count, height)
    return pattern


def main():
    height = int(input("\n\tEnter the number of lines for the pyramid: "))
    brick_character = \
        input("\tEnter the character from which the pyramid should be made: ")
    print(pyramid_string(brick_character, height))


# Start the program
if __name__ == "__main__":
    main()

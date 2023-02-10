"""
    This program prompts the user for the height of a diamond and prints it.

    Author: Rae Harbird
    The problem was created by Rob Miller, DIS, UCL for a Java course.
    Date: August 2018
"""

MARGIN = 10


def pyramid_line(symbol, line_number, height):
    """
    Construct string representing a line of the pyramid and return the string.

    Parameters
    ----------
    symbol : str
        Symbol from which the pyramid is composed
    line_number : int
        The current line number
    height : int
        The height of the pyramid

    Returns
    -------
    str
        string representing a line of the pyramid

    """
    line = ""
    line += spaces_for_pyramid_line(line_number, height)
    line += symbols_for_pyramid_line(symbol, line_number)
    line += "\n"
    return line


def symbols_for_pyramid_line(symbol, line_num):
    """
    Construct string representing the symbols for a line of the pyramid. Return the string.

    Parameters
    ----------
    symbol : str
        The symbol from which the pyramid will be printed
    line_num : int
        the line number

    Returns
    -------
    str
        the symbols for the current line

    """
    line_symbols = ""
    for symbols_count in range((line_num * 2) - 1):
        line_symbols += symbol
    return line_symbols


def spaces_for_pyramid_line(line_num, height):
    """
    Construct string representing the spaces for a line of the pyramid and return the string.

    Parameters
    ----------
    line_num : int
        the number of the line
    height : int
        the height of the pyramid

    Returns
    -------
    str
        the symbols for the current line
    """
    line_spaces = ""
    for spaces_count in range(MARGIN + height + 1 - line_num):
        line_spaces += " "
    return line_spaces


def pyramid_string(character, height):
    """
    Construct string representing the pyramid, return the string.

    Parameters
    ----------
    character : str
        the character from which the pyramid will be built

    height : int
        the height of the pyramid

    Returns
    -------
    str
        the symbols for the current line

    """
    pattern = ""
    for lineCount in range(1, height + 1):
        pattern += pyramid_line(character, lineCount, height)
    return pattern


def diamond_string(brick_character, height):
    """
    Construct string representing the diamond, return the string

    Parameters
    ----------
    brick_character : str
        the character from which the diamond will be built

    height : int
        the height of the diamond

    Returns
    -------
    str
        the string for the current diamond

    """
    pyramid_height = height // 2
    diamond_str = ""
    diamond_str += pyramid_string(brick_character, pyramid_height + 1)
    diamond_str += upside_down_pyramid_string(brick_character, pyramid_height)
    return diamond_str


def upside_down_pyramid_string(brick_character, height):
    """
    Construct string representing the inverted pyramid

    Parameters
    ----------
    brick_character : str
        the character from which the pyramid will be built

    height : int
        the height of the pyramid

    Returns
    -------
    str
        the string for the upside-down pyramid part of the diamond

    """
    pattern = ""
    for line_count in reversed(range(1, height + 1)):
        pattern += pyramid_line(brick_character, line_count, height + 1) ##
    return pattern


def main():
    height = int(input("\n\tEnter the number of lines for the diamond: "))
    brick_character = input("\tEnter the character from which the diamond should be made: ")
    if height % 2 != 1:
        height += 1
    print(diamond_string(brick_character, height))


# Start the program
if __name__ == "__main__":
    main()

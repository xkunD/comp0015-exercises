MARGIN = 10

def pyramid_line(symbol, line_number, height):    
    line = ""
    line += spaces_for_pyramid_line(line_number, height)
    line += symbols_for_pyramid_line(symbol, line_number)
    line += "\n"
    return line


def symbols_for_pyramid_line(symbol, line_num):    
    line_symbols = ""
    line_symbols += symbol * ((line_num * 2) - 1)
    return line_symbols


def spaces_for_pyramid_line(line_num, height):
    line_spaces = ""
    line_spaces += " " * (MARGIN + height + 1 - line_num)
    return line_spaces


def pyramid_string(character, height):
    pattern = "\n"
    for line_count_up in range(1, int((height + 1)/2)+1, 1):
        pattern += pyramid_line(character, line_count_up, height)
    for line_count_down in range(int((height + 1) /2), 0, -1):
        pattern += pyramid_line(character, line_count_down, height)
    
    return pattern



def main():
    height = int(input("\n\tEnter the number of lines for the pyramid: "))
    brick_character = \
        input("\tEnter the character from which the pyramid should be made: ")
    print(pyramid_string(brick_character, height))


# Start the program
if __name__ == "__main__":
    main()

def swap_pairs(the_string):
    """
    Returns a string in which pairs of letters are swapped.
    If the string has an odd number of letters, leave the last
    letter in place.
    """

    offset = 1
    
    if len(the_string) % 2 == 1:
        offset = 2

    new_string = ""
    
    for i in range(0, len(the_string) - offset, 2):
        new_string += the_string[i + 1]
        new_string += the_string[i]
        

    return new_string
        

def main():
    print(swap_pairs("example"))
    print(swap_pairs("another example."))

if __name__ == "__main__":
    main()

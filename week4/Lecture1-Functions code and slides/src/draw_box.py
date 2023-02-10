
# Prints a rectangular box.
def draw_box(width, height):
    '''Print a box of given width and height.'''
    print("*" * width)
    for line in range(height - 2):
        print("*", "." * (width - 2), "*", sep="")
    print("*" * width)


def box(width = 3, height = 3):
    '''Print a box of given width and height.'''
    print("*" * width)
    for line in range(height - 2):
        print("*", "." * (width - 2), "*", sep="")
    print("*" * width)


def main():
    box(5,10)
    print()
    box()
    print()
    box(5)



        

    
    

if __name__ == "__main__":
    main()

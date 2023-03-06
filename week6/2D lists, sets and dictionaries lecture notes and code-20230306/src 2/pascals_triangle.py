# This program creates a jagged two-dimensional list
# that stores Pascal's Triangle. It takes advantage of the
# fact that each value other than the 1s that appear at the
# beginning and end of each row is the sum of two values
# from the previous row.

# Fills Pascal's triangle into the given 2D list up to
# the size of that list.
# Authors: Stepp, Obourn, Regis from "Building Python Programs"
def fill_in(triangle):
    for i in range(len(triangle)):
        triangle[i] = [0] * (i + 1)
        triangle[i][0] = 1
        triangle[i][i] = 1
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] \
                           + triangle[i - 1][j]

# Prints a 2D list with one row on each line
# with elements separated by spaces.
def print_nice(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            print(triangle[i][j], end=" ")
        print()

def main():
    triangle = [0] * 11
    fill_in(triangle)
    print_nice(triangle)

main()

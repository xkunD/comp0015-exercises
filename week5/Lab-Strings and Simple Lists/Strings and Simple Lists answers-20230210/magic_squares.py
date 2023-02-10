def check_left_diagonal(square, dimension_sum, length):

    ld_sum = 0
    
    for j in range(length):
        ld_sum += square[j][j]
        
    return ld_sum == dimension_sum


def check_right_diagonal(square, dimension_sum, length):
    column = length - 1
    rd_sum = 0
    
    for row in range(length):
        rd_sum += square[row][column]
        column = column - 1    

    return rd_sum == dimension_sum


def check_row_sum(square, dimension_sum, length):
    rows_same = True

    for i in range(length):
        sum_of_row = 0

        for j in range(length):
            sum_of_row += square[i][j]
        
        if sum_of_row != dimension_sum:
            rows_same = False
            break          
        
    return rows_same


def check_column_sum(square, dimension_sum, length):
    
    columns_same = True

    for j in range(length):
        sum_of_column = 0

        for i in range(length):
            sum_of_column += square[j][i]
        
        if sum_of_column != dimension_sum:
            columns_same = False
            break          
        
    return columns_same


def is_magic_square(sq):

    # Assume array is square, find the dimension
    square_length = len(sq[0])

    # Find the sum of first column
    target_sum = 0
    for i in range(square_length):
        target_sum += sq[0][i]

    # Now check all dimensions
    
    # Columns 
    col_sum_same = check_column_sum(sq, target_sum, square_length)

    # Rows 
    row_sum_same = check_row_sum(sq, target_sum, square_length)
    
    # Left diagonal - top left to bottom right    
    left_diagonal_same = check_left_diagonal(sq, target_sum, square_length)

    # Right diagonal - top right to bottom left    
    right_diagonal_same = check_right_diagonal(sq, target_sum, square_length)

    is_magic = col_sum_same and row_sum_same and left_diagonal_same and right_diagonal_same
        
    return is_magic
    

# Magic squares
def main():
    
    square1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    square2 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    square3 = [[3, 4, 5], [3, 5, 4], [5, 4, 3]]
    square4 = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

    works1 = is_magic_square(square1)
    print("square1 is magic:", works1)
    works2 = is_magic_square(square2)
    print("square2 is magic:", works2)
    works3 = is_magic_square(square3)
    print("square3 is magic:", works3)
    works4 = is_magic_square(square4)
    print("square4 is magic:", works4)


if __name__ == "__main__":
    main()

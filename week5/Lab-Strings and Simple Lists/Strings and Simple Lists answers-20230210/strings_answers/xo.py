"""

COMP0015
Prints a pattern of x and o to form a cross

"""

def xo(n):
    for row in range(n):
        for col in range(n):
            if col == row or col == (n - row) - 1:
                print('x', end = '')
            else:
                print('o', end = '')
        print()
    print()




def main():
    xo(5)
    xo(6)





if __name__ == "__main__":
    main()

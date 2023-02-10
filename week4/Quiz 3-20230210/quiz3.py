"""
    This program describes a function that takes as a parameter an integer n > 1 
    and prints on the screen all perfect numbers strictly less than n.

    Author: Elaine Pimentel
    Date: February 2023
"""


def perfect(n):
    """
    Takes an integer n>1 as parameter and prints on the screen all perfect numbers strictly less than n

    """
    for poss_perfect in range(1,n) :
        sum_div = 0
        for poss_div in range(1,poss_perfect) :
            if poss_perfect % poss_div == 0 :
                sum_div += poss_div
        if sum_div == poss_perfect :
            print(poss_perfect, " ", end="") 
            """"
            Note that this will add the symbol of the shell prompt at the end of the printing (e.g. mine is "%")
            This is because there is no newline at the end of the output, so whatever gets printed next 
            appears immediately after the final character from the loop.
            There are many ways to avoid that, but this is a quick answer to the quiz.
            """"


def main():
    n = int(input("Enter an integer n>1: "))
    perfect(n)


# Start the program
if __name__ == "__main__":
    main()

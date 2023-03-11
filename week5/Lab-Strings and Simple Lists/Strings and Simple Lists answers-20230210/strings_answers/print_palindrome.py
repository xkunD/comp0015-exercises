"""

COMP0015
Checks whether a string is a palindrome

"""

def print_palindrome(string):

    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
        
    if reversed_string.lower() == string.lower():
        print(f"\n'{string}' is a palindrome")
    else:
        print(f"\n'{string}' is not a palindrome")
    




def main():
     print_palindrome("Abba")
     print_palindrome("racecar")
     print_palindrome("COMP0015")





if __name__ == "__main__":
    main()

"""
File: list_range.py

 Description: prints the range of values in a list of integers.
 Range is defined as 1 more than the difference between the maximum and minimum values in the list.

 Author: Rae Harbird

 Date: August 2018
"""


def list_range(the_list):
    min_value = min(the_list)
    max_value = max(the_list)
    
    return max_value - min_value + 1
        
        
def main():
    my_list = [36, 12, 25, 19, 46, 31, 22]
    print("The range of list: {} is: {}.".format(my_list, list_range(my_list)))


# Start the program
if __name__ == "__main__":
    main()

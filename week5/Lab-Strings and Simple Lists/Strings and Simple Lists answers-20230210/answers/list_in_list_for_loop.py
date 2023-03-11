"""File: list_in_list.

Author: Rae Harbird

Date: August 2018

Check lists valid. Return True if the longer list is equal in length or longer than the other list.
"""



def lists_valid(long_list, short_list):
    """
    @param long_list the longer list
    @param short_list the shorter list
    @return True or False
    """
    if len(long_list) == 0 or len(short_list) == 0:
        return False
   
    if len(short_list) > len(long_list):
        return False
    
    return True

   
def contains(longer_list, shorter_list):
    """
    Returns True if the shorter list is contained in the longer list
    This is a shorter version of the code above

    @param longerList the longer list
    @param shorterList the shorter list
    @return True or False
    """
    
    # Check that the lists are valid
    if not lists_valid(longer_list, shorter_list):
        return False
    
    # Return as soon as we have a match
    shorter_list_length = len(shorter_list)
    for i in range((len(longer_list) - shorter_list_length) + 1):
        if longer_list[i:i + shorter_list_length] == shorter_list:
            return True
        
    return False


def main():
    print("\n\nTest 1:")
    list1 = [1, 6, 2, 3, 4, 1, 2, 1, 8]
    list2 = [2, 1, 8]

    print("List1 : {}".format(list1))
    print("List2 : {}".format(list2))

    if contains(list1, list2):
        print("List 2 contained in list 1")
    else:
        print("List 2 not contained in list 1")

    print("\n\nTest 2:")
    list2 = [1, 6, 2, 3, 4, 1, 2, 1, 8]
    list1 = [2, 1, 8]

    print("List1 : {}".format(list1))
    print("List2 : {}".format(list2))

    if contains(list1, list2):
        print("List 2 contained in list 1")
    else:
        print("List 2 not contained in list 1")

    print("\n\nTest 3:")
    list1 = []
    list2 = []

    print("List1 : {}".format(list1))
    print("List2 : {}".format(list2))

    if contains(list1, list2):
        print("List 2 contained in list1")
    else:
        print("List 2 not contained in list1")

    print("\n\nTest 4:")
    list1 = [1, 6, 2, 3, 4, 1, 2, 1, 8]
    list2 = [2, 1, 7]    

    print("List1 : {}".format(list1))
    print("List2 : {}".format(list2))

    if contains(list1, list2):
        print("List 2 contained in list1")
    else:
        print("List 2 not contained in list1")


if __name__ == "__main__":
    main()

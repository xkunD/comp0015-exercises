# Name: delete_small_words_with_for.py
# 
# Description
# This program uses a 'for' loop when deleting elements in a list of words that
# are less than 4 characters long.
# 
# It does not work because the we are modifying the length of the list after we
# have set the number of iterations for the loop.
# 
# #

# # Start the program
def main():
    words = ["Welcome", "to", "the", "island!"]

    print("\n", words)
    for i in range(len(words)) :
        word = words[i]
        print("\ti: {}, {}".format(i, words[i]))
        if len(word) < 4 :      
            words.pop(i) 

    print("\n", words)

if __name__ == "__main__":
    main()
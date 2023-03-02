##
# Name: delete_small_words_with_while.py
# 
# Description
# This program uses a 'while' loop when deleting elements in a list of words that
# are less than 4 characters long.# 
##

# Start the program
def main():
    words = ["Welcome", "to", "the", "island!"]

    print("\n", words)
    i = 0
    print()
    
    while i < len(words) :
        print("\ti: {}, {}".format(i, words[i]))
        word = words[i]
        if len(word) < 4 :      
            words.pop(i) 
        else :
            i = i + 1

    print("\n", words)

if __name__ == "__main__":
    main()

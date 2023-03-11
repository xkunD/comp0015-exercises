"""
COMP0015
Repeats a string a given number of times
"""

def repl(string, num_times):
    result = ""
    for i in range(num_times):
        result += string
    return result




def main():
    print(repl("Hello", 6))





if __name__ == "__main__":
    main()

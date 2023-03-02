from turtle import *
import math
import random



# question 7
def is_all_char_in(str1, str2):
    for i in range(len(str1)):

        char = str1[i].lower()
        j = 0
        foundit = False
        while j < len(str2) and foundit == False :
            if char == str2[j].lower():
                #print(char,"equal to",str2[j])
                foundit = True
            else:
                #print(char,"compare to",str2[j])
                j += 1
        if foundit == False:
            return 0
    return 1

# question 6
def three_heads():
    heads = 0
    while heads < 3:
        n = random.randint(0, 1)
        if n == 0 :
            print("H", end = ' ')
            heads += 1
        else:
            print("T", end = " ")
            heads = 0
    print("\nCongratulations!")

def question5():
    penup()
    setpos(-50,0)
    pendown()
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    penup()
    lt(135)

    fd(50*math.sqrt(2))
    rt(135)
    fd(50*math.sqrt(2))
    
    lt(135)
    pendown()
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(45)



# question 4
def remove_eq(nums, n):
    removed = True
    while removed:
        removed = False
        if n in nums:
            nums.remove(n)
            removed = True
    return nums

# question 3
def g(s):
    str_len = len(s)
    half_len = int(str_len/2)

    count = 0
    i = 0
    not_broken = True
    while i < half_len and not_broken:
        if s[i] == s[str_len - 1 - i].lower():
            count += 1
        else:
            not_broken = False
        i += 1
    return count



def main():

    # print(g("Abab"))
    # print(g("redivider"))
    # print(g("rAcecaR"))

    print(remove_eq([18, 7, 8, 34, 8, 8, 23], 8))
    print(remove_eq([8, 8, 8], 8))
    print(remove_eq([18, 7, 8, 34, 8, 8, 23], 38))

    #question5()

    # three_heads()
    
    print(is_all_char_in("wHol", "Hello world"))
    print(is_all_char_in("eo2u", "Hello world"))
    print(is_all_char_in("whol", "Hello world"))
    print(is_all_char_in("wHoooo elHd", "Hello world"))
    print(is_all_char_in("", "Hello world"))
    print(is_all_char_in("Hello World", "Hello world"))

if __name__ == '__main__':
    main()
import math

def isPerfectNumber(n):
    sum =1
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            if n % i == i:
                sum += i
            else:
                sum += i
                sum += n//i
        i = i + 1
    # print(n,"have list of factors of",factors)
    return True if sum == n else False

def printPerfectNumber(n):
    for i in range (2, n):
        if isPerfectNumber(i):
            print(i)

def main():
    print("please enter the value of n: ")
    n = int(input())
    print("Perfect Numbers Are: ")
    printPerfectNumber(n)

if __name__ == "__main__":
    main()

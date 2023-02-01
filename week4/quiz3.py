import math

def isPerfectNumber(n):
    factors = []
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            if n % i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(int(n/i))
        i = i + 1
    # print(n,"have list of factors of",factors)
    return True if sum(factors)+1 == n else False

def printPerfectNumber(n):
    for i in range (1, n+1):
        if isPerfectNumber(i):
            print(i)

def main():
    print("please enter the value of n: ")
    n = int(input())
    print("Perfect Numbers Are: ")
    printPerfectNumber(n)

if __name__ == "__main__":
    main()

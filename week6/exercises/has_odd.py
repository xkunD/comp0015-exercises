def has_odd(set):
    for number in set:
        if number % 2 == 1:
            return True
    return False

def main():
    set0 = {1, 2, 4, 6}
    set1 = {2, 4, 6}
    set3 = set()
    print(has_odd(set0), has_odd(set1), has_odd(set3))


if __name__ == "__main__":
    main()
def is_1_to_1(dic):
    values_seen = set()
    for value in dic.values():
        if value not in values_seen:
            values_seen.add(value)
        else:
            return False
    return True

def main():
    dic1 = {"Marty": "206-9024", "Hawking": "123-4567", "Smith": "949-0504", "Newton": "123-4567"}
    dic2 = {"Marty": "206-9024", "Hawking": "555-1234", "Smith": "949-0504", "Newton": "123-4567"}
    dic3 = {}
    print(is_1_to_1(dic1))
    print(is_1_to_1(dic2))
    print(is_1_to_1(dic3))

if __name__ == "__main__":
    main()


def intersect(dic1, dic2):
    intersect = {}
    for key1, value1 in dic1.items():
        for key2, value2 in dic2.items():
            if key1 == key2 and value1 == value2:
                intersect[key1] = value1
    return intersect
                

def main():
    dic1 = {"Janet": 87, "Logan": 62, "Whitaker": 46, "Alyssa": 100, "Stef": 80,"Jeff": 88, "Kim": 52, "Sylvia": 95}
    dic2 = {"Logan": 62, "Kim": 52, "Whitaker": 52, "Jeff": 88, "Stef": 80, "Brian":60, "Lisa": 83, "Sylvia": 87}
    print(intersect(dic1, dic2))

if __name__ == "__main__":
    main()
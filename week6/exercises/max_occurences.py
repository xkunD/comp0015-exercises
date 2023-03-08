def max_occurences(list):
    dic = {}
    res_pair = ()
    max_count = 1
    for number in list:
        if number in dic:
            dic[number] += 1
            if dic[number] > max_count:
                max_count = dic[number]
                res_pair = (number, max_count)
        else:
            dic[number] = 1

    return res_pair

def main():
    list = [9, 7, 6, 2, 7, 6, 9, 4, 2, 8, 5, 5, 3, 7, 6, 3, 0, 2, 2, 2, 7, 3, 6, 5, 2, 1, 2, 6, 8, 0, 5, 4, 1, 9, 1, 0, 6, 5, 1, 8, 0, 5, 2, 2, 0, 3, 0, 4, 8, 8, 3, 3, 8, 6, 8, 6, 6, 9, 2, 7, 9, 1, 0, 6, 1, 5, 4, 8, 7, 0, 7, 6, 4, 3, 6, 7, 9, 4, 9, 6, 4, 4, 0, 0, 7, 2, 2, 2, 1, 4, 1, 5, 5, 3, 0, 9, 5, 3, 1, 4]
    print(max_occurences(list))

if __name__ == "__main__":
    main()
    
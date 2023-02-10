
def main():
    year_now = int(input("Enter the current year then press RETURN: "))
    age_now = int(input("Enter your current age in years: "))
    another_year = int(input("Enter the year in which you wish to know your age: "))
    another_age = another_year - (year_now - age_now)
    if another_age > 150:
        print("Sorry, but you'll probably dead by " + str(another_year) + " !")
    elif another_age < 0:
        print("You weren't born in {} !".format(year_now - age_now))
    else:
        print("Your age in {}: {}".format(another_year, another_age))
    
if __name__ == "__main__":
    main()
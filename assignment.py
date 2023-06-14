def smaller(leap_year, year):
        return leap_year - year

def bigger(year, leap_year):
        return year - leap_year
leap_year = 2024
year = input("Enter the year: ")

if year <= leap_year:
        smaller(leap_year, year)
        small = (smaller)
        if small % 4 == 0:
                print("The year", year, "is a leap year")

        else:
                print("the year", year, "is not a leap year")

elif year >= leap_year:
        bigger(year, leap_year)
        big = (bigger)
        if big % 4 == 0:
                print("The year", year, "is a leao year")

        else:
                print("The year", year, "is not a leap year")


elif year == leap_year:
        print("The year", year, "is a leap year")


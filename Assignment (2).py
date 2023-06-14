import datetime
current_year = datetime. datetime.now().year

def year_dif(current_year, year):
    return current_year - year

year = int(input("Enter your year of birth: "))

result = year_dif(current_year, year)

if result == 18:
    print("You can vote")

else:
    print("You are not old enough")
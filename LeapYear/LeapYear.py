#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):
    leap = False

    # Write your logic here

    not_leap_years = [1800, 1900, 2100, 2200, 2300, 2500]
    leap_years = [2000, 2400]

    if year == not_leap_years:
        leap = False
    elif year != not_leap_years:
        if year % 4 == 0:
            leap = True
        if year % 100 == 0:
            leap = False
        if year % 400 == 0:
            leap = True
        elif year % 4 == 0:
            if year % 100 == 0:
                leap = False
        elif year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
    if year == leap_years:
        leap = True
    return leap


year = int(input('Введите год\n'))
print(is_leap(year))
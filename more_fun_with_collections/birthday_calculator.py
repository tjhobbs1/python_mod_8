"""
Program:  birthday_calculator.py
Author:  Ty Hobbs
Last Day Modified:  10/15/2019

The purpose of the program is to take in a birthday and return the date of the half birthday.

"""
import datetime
import calendar


def half_birthday(date):
    """
    This function takes in a birthday an then determines if it is a leap years and calculates the what the half
    birthday should be.
    :param date: Is the passed in birthday.
    :return:  The half birthday.
    """
    if calendar.isleap(date.year):              # Test to see if the year is a leap year.
        half_birthday_date = date + datetime.timedelta(183)
        half_birthday_date = half_birthday_date.strftime("%B %d")
        return half_birthday_date
    else:
        half_birthday_date = date + datetime.timedelta(182.5)
        half_birthday_date = half_birthday_date.strftime("%B %d")
        return half_birthday_date


if __name__ == '__main__':
    birthday = datetime.date(1800, 6, 1)
    print(half_birthday(birthday))

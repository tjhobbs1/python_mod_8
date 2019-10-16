"""
Program:  set_membership.py
Author:  Ty Hobbs
Last Day Modified:  10/011/2019

The purpose of the program is cross check a set of values with another value and return a boolean of truthy if it finds
it else falsy if it does not find a match.

"""


def in_set(passed_set_of_numbers,checked_value):
    """
    This function takes in a set of values and a passed value and returns a boolean of falsy if the passed value
    is not in the function or truthy if it is.
    :param passed_set_of_numbers: is the passed set of values
    :param checked_value: is the value that is passed into that is being checked against the set.
    :return: a boolean
    """
    if checked_value in passed_set_of_numbers:  # Checks the passed value against the set of values.
        return True
    else:
        return False


if __name__ == '__main__':
    set_of_numbers = {6,7,8,9,6,9,56,"cat","dog",-99,678,45.6,23,87,"Ty","Yellow",False,(1,2,3)}

    print(in_set(set_of_numbers,"cat"))     # Returns True
    print(in_set(set_of_numbers,15))        # Return False
    print(in_set(set_of_numbers,True))      # Returns False
    print(in_set(set_of_numbers,False))     # Returns True
    print(in_set(set_of_numbers,(1,2,3)))   # Returns True
    print(in_set(set_of_numbers,-99))       # Returns True
    print(in_set(set_of_numbers,-77))       # Returns False
    print(in_set(set_of_numbers,(7,8,9)))   # Returns False



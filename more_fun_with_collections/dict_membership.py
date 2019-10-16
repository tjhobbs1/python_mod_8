"""
Program:  dict_membership.py
Author:  Ty Hobbs
Last Day Modified:  10/15/2019

The purpose of the program is to see if a value is located in the dictionary.  It will return truthy if it finds the
value and falsy if it does not.

"""


def in_dict(passed_in_dict, passed_in_test_value):
    """
    The purspose of this function is to take in a dictionary and passed in value and checks to see if the value
    is located in the dictionary.
    :param passed_in_dict: a dictionary of values
    :param passed_in_test_value: a value to check to see if the value exist in the dictionary.
    :return: a boolean of weather the value is in the dictionary or not.
    """
    if passed_in_test_value in passed_in_dict.values():
        return True
    else:
        return False



if __name__ == '__main__':
    employees = {101:'Ty', 102:'Jim',103:'Sue',104:'Ted'}

    print(in_dict(employees,'Ty'))  # Returns True
    print(in_dict(employees,103))   # Returns False
    print(in_dict(employees,'Sue')) # Returns True
    print(in_dict(employees,-1))    # Returns False

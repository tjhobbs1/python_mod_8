"""
Program:  assign_average.py
Author:  Ty Hobbs
Last Day Modified:  10/15/2019

The purpose of the program is to take in a letter grade of A-F and returns the minimum score possible needed to achieve
that grade.

"""
def switch_average(letter_grade):
    """
    This function takes in a letter grade and returns the minimum score needed to obtain that grade.
    :param letter_grade: A letter grade.
    :return: The minimum score needed to achieve that letter grade. Returns "Not a valid grade" if a non-letter grade
    is passed in.
    """
    options = {
        "A" : 90,
        "B" : 80,
        "C" : 70,
        "D" : 60,
        "F" : 50
        }
    lowest_score_possible = options.get(letter_grade,"Not a valid grade")
    return lowest_score_possible


if __name__ == '__main__':
    print(switch_average("F"))  # Returns 50
    print(switch_average("A"))  # Returns 90
    print(switch_average("C"))  # Returns 70
    print(switch_average("Z"))  # Returns Not a valid grade
    print(switch_average(7))    # Returns Not a valid grade


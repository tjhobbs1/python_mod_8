"""
Program: validate_input_functions.py
Author: Ty Hobbs
Last date modified: 09/30/2019



The purpose of this program is to use the function score_input to determine if the test score is valid.
It checks to make sure that the test score is greater than 0 and less than 100 and that it is either a float
or an int.
"""

def score_input(test_name, test_score=0, invalid_message="Invalid test test_score, try again!"):
    # Takes a test_name string, test score and an error message and checks to see if the test score is a valid format.
    # :param test_name: String that takes the name of the test.
    # :param test_score:  Takes the value of the test score that is being tested.  Default of 0.
    # :param invalid_message:  Takes the value of the invalid message to return user. Has a default of "Invalid test test_score, try again!"
    # :returns the test name and test score if valid, if not it will return an error message and keep asking the user to enter a valid test score.

    num_scores = int(input("Enter the number of scores you need to enter: "))
    passed_score = float(input("Enter a test score: "))
    scores_dict = dict()

    while num_scores >= 0:
        while type(passed_score) not in[float, int]:   # Check to make sure the passed_score is either a float or an int.
            try:
                float(passed_score)
            except ValueError:
                print(invalid_message)   # Throw an error if a ValueError is raised.
                passed_score = input("Enter a valid test score1: ")
            else:
                float(passed_score)
                break
        passed_score = float(passed_score)  # Cast passed score to a float.

        while (passed_score < 0) or (passed_score > 100):    # Check to see if the number is a negative number or greater than 100.
            try:
                passed_score = float(input("Enter a valid test score: "))
            except ValueError:
                print(invalid_message)
        else:
           scores_dict.update(passed_score)
           num_scores = num_scores -1



if __name__ == '__main__':

   score_input(test_name = input("Enter the test name: "))


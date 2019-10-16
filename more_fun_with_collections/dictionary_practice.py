"""
Program: validate_input_functions_dictionary.py
Author: Ty Hobbs
Last date modified: 10/16/2019



The purpose of this program is to use the function score_input to determine if the test score is valid.
It checks to make sure that the test score is greater than 0 and less than 100 and that it is either a float
or an int.  It then stores the values in a dictionary and then returns the average of the test scores that are entered.
"""


def score_input(test_name, scores_dict, invalid_message="Invalid test test_score, try again!"):
    # Takes a test_name string, test score and an error message and checks to see if the test score is a valid format.
    # :param test_name: String that takes the name of the test.
    # :param test_score:  Takes the value of the test score that is being tested.  Default of 0.
    # :param invalid_message:  Takes the value of the invalid message to return user. Has a default of "Invalid test test_score, try again!"
    # :returns the test name and test score if valid, if not it will return an error message and keep asking the user to enter a valid test score.

    num_scores = int(input("Enter the number of scores you need to enter: "))

    scores_dict1 = dict()

    for a in range(num_scores):
        passed_score = input("Enter a test score: ")
        while type(passed_score) not in[float, int]:   # Check to make sure the passed_score is either a float or an int.
            try:
                float(passed_score)
            except ValueError:
                print(invalid_message)   # Throw an error if a ValueError is raised.
                passed_score = input("Enter a valid test score: ")
            else:
                passed_score = float(passed_score)
                break
        passed_score = float(passed_score)  # Cast passed score to a float.

        while (passed_score < 0) or (passed_score > 100):    # Check to see if the number is a negative number or greater than 100.
            try:
                passed_score = float(input("Enter a valid test score: "))
            except ValueError:
                print(invalid_message)
        else:
           num_scores = num_scores-1
           scores_dict1[num_scores]=passed_score

    average_scores(test_name,scores_dict1)


def average_scores(test_name_passed,dict_of_scores):
    """
    The purpose of this function is to take in a dictionary of test scores and then finds the average of the test scores.
    :param test_name_passed: name of the test that the average is being performed on.
    :param dict_of_scores: dictionary of test scores.
    :return: the name of the test with the average of the test scores. 
    """
    dict_length = len(dict_of_scores)
    sum = 0
    for i in dict_of_scores :
        sum = sum + dict_of_scores[i]

    average_scores = (sum/dict_length)
    print(test_name_passed, "average score is ",average_scores)


if __name__ == '__main__':

   test_name_entered = input("Enter the test name: ")
   scores_dict = dict()
   score_input(test_name_entered,scores_dict)










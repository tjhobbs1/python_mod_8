def switch_average(letter_grade):
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
    print(switch_average("F"))

def in_dict(passed_in_dict, passed_in_test_value):
    if passed_in_test_value in passed_in_dict.values():
        return True
    else:
        return False



if __name__ == '__main__':
    employees = {101:'Ty', 102:'Jim',103:'Sue',104:'Ted'}
    print(in_dict(employees,'Ty'))

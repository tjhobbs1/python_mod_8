"""
Program:  test_birthday_calculator.py
Author:  Ty Hobbs
Last Day Modified:  10/15/2019

The purpose of the program is to test the function half_birthday in the birthday_calculator.py file.

"""
import unittest
import more_fun_with_collections.birthday_calculator as birthday
import datetime



class Grade_Test(unittest.TestCase):
    def test_switch_statement(self):
        self.assertEqual(birthday.half_birthday(datetime.date(2000, 1, 19)),"July 20")
        self.assertEqual(birthday.half_birthday(datetime.date(1981, 3, 19)),"September 17")
        self.assertEqual(birthday.half_birthday(datetime.date(2024, 12, 15)),"June 16")
        self.assertEqual(birthday.half_birthday(datetime.date(1800, 6, 1)),"November 30")


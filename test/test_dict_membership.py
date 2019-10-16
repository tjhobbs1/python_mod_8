"""
Program:  test_dict_membership.py
Author:  Ty Hobbs
Last Day Modified:  10/15/2019

The purpose of the program is to test the function in dict_membership.

"""

import unittest
import more_fun_with_collections.dict_membership as membership

class dictionaryTest(unittest.TestCase):

     def test_in_dict_true(self):
         self.assertTrue(membership.in_dict({101:'Ty', 102:'Jim',103:'Sue',104:'Ted'},'Ted'))
         self.assertTrue(membership.in_dict({101:'Ty', 102:'Jim',103:'Sue',104:'Ted'},'Ty'))
         self.assertTrue(membership.in_dict({101:'Ty', 102:'Jim',103:'Sue',104:'Ted'},'Ted'))

     def test_in_dict_false(self):
         self.assertFalse(membership.in_dict({101:'Ty', 102:'Jim',103:'Sue',104:'Ted'},'Jason'))
         self.assertFalse(membership.in_dict({101:'Ty', 102:'Jim',103:'Sue',104:'Ted'},101))
         self.assertFalse(membership.in_dict({101:'Ty', 102:'Jim',103:'Sue',104:'Ted'},-1))

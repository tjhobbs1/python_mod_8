"""
Program:  test_set_membership.py
Author:  Ty Hobbs
Last Day Modified:  10/011/2019

The purpose of the program is to test the in_set function from set_membership.py

"""

import unittest
import more_fun_with_collections.set_membership as membership


class CollectionsTest(unittest.TestCase):
    # Check to if the function in_set will return truthy of the number is in the set.
    def test_in_set_true(self):
        self.assertTrue(membership.in_set({6,7,8,9},9))                         # Test ints
        self.assertTrue(membership.in_set({1,1,1,1},1))                         # Test all the same numbers in the set.
        self.assertTrue(membership.in_set({-1,-2,-67,12345},-2))                # Test negative numbers
        self.assertTrue(membership.in_set({10.24,6.45,87.99,124.567},10.24))    # Test floats
        self.assertTrue(membership.in_set({6,"Dog",68.9,-1,"345"},"Dog"))       # Test combo float, int, Strings with check of a String
        self.assertTrue(membership.in_set({6,"Dog",68.9,-1,"345"},"345"))       # Test combo float, int, Strings with a check of String Number
        self.assertTrue(membership.in_set({6,"Dog",68.9,-1,"345"},-1))          # Test combo float, int, Strings with check of negative int.
        self.assertTrue(membership.in_set({56,True,"Cat",56-1,0},True))         # Test a Boolean
        self.assertTrue(membership.in_set({56,(1,2,3),"Cat",56-1},56-1))        # Test subtraction in a value
        self.assertTrue(membership.in_set({56,(1,2,3),"Cat",56-1,("Ty","Sara","Joe")},("Ty","Sara","Joe")))        # Test Tuples

    # Check to see if the function in_set will return falsy if the number isn't in the set.
    def test_in_set_false(self):
        (self.assertFalse(membership.in_set({6,7,8,9},99)))                   # Test ints
        self.assertFalse(membership.in_set({1,1,1,1},10))                   # Test all the same numbers in the set.
        self.assertFalse(membership.in_set({-1,-2,-67,12345},-267))         # Test negative numbers
        self.assertFalse(membership.in_set({10.24,6.45,87.99,124.567},10))  # Test Float
        self.assertFalse(membership.in_set({6,"Dog",68.9,-1,"345"},"Cat"))  # Test combo float, int, Strings with check of a String
        self.assertFalse(membership.in_set({6,"Dog",68.9,-1,"345"},"777"))  # Test combo float, int, Strings with a check of String Number
        self.assertFalse(membership.in_set({6,"Dog",68.9,-1,"345"},-10))    # Test combo float, int, Strings with check of negative int.
        self.assertFalse(membership.in_set({56,True,"Cat",56-1,0},89))      # Test a Boolean
        self.assertFalse(membership.in_set({56,True,"Cat",56-1,0},56-8))      # Test a substracted number
        self.assertFalse(membership.in_set({56,(1,2,3),"Cat",56-1,("Ty","Sara","Joe")},("Ty","Sara","Tim")))        # Test Tuples


if __name__ == '__main__':
    unittest.main()

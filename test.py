#!/usr/bin/python3
# Test file for basic arithmetic operations on two numbers

import unittest
from main import *

class TestOperations(unittest.TestCase):
    def test_addition(self):
        """
        Test case 1 for checking addition operation on given two numbers
        """
        data = [5,6]
        result = addition(data)
        self.assertEqual(result, 11)
        
    def test_subtraction(self):
        """
        Test case 2 for checking subtraction operation on given two numbers
        """
        data = [5,6]
        result = subtraction(data)
        self.assertEqual(result, 1)
    
    def test_multiplication(self):
        """
        Test case 3 for checking multiplication operation on given two numbers
        """
        data = [5,6]
        result = multiplication(data)
        self.assertEqual(result, 30)
    
    def test_quotient(self):
        """
        Test case 4 for checking quotient operation on given two numbers
        """
        data = [5,6]
        result = quotient(data)
        self.assertEqual(result, 0)
        
    def test_remainder(self):
        """
        Test case 5 for checking remainder operation on given two numbers
        """
        data = [5,6]
        result = remainder(data)
        self.assertEqual(result, 5)

    
if __name__ == '__main__':
    unittest.main()

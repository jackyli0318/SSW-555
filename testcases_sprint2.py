#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:57:53 2018

@author: jackylee
"""

import unittest
from sprint2 import check_150


class Test_Check_150(unittest.TestCase):
    ''' Test check_150.py'''
    
    def test_150less(self):
        print("\nAlive testing:\n")
        self.assertEqual(0, check_150(0))
        self.assertEqual(80, check_150(80))
        self.assertEqual(149, check_150(149))
        self.assertEqual(150, check_150(150))
        self.assertEqual(1, check_150(1))
        
    def test_150more(self):
        print("\nDead testing:\n")
        self.assertEqual("NA", check_150(151))
        self.assertEqual("NA", check_150(160))
        self.assertEqual("NA", check_150(3000))
    
        
    
    
if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
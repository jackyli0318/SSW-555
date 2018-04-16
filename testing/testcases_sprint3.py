#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:57:53 2018

@author: jackylee
"""

import unittest
from sprint3 import birth_before_death, marr_before_death, get_married_lst, get_living_lst, get_single_lst, list_deceased, list_recent_birth


class Test_birth_before_death(unittest.TestCase):
    ''' Test birth_before_death'''
    
    def test_correct(self):
        print("\nAlive testing:\n")
        self.assertEqual(True, birth_before_death("2018-09-20", "2019-02-02"))
        self.assertEqual(True, birth_before_death("1908-09-22", "1919-04-12"))
        self.assertEqual(True, birth_before_death("1918-11-30", "1929-05-22"))
        self.assertEqual(True, birth_before_death("1998-2-10", "1999-07-06"))
        self.assertEqual(True, birth_before_death("2008-1-1", "2009-10-05"))
        
    def test_wrong(self):
        print("\nDead testing:\n")
        self.assertEqual(False, birth_before_death("2018-09-20", "2009-02-02"))
        self.assertEqual(False, birth_before_death("2021-01-20", "1999-02-02"))
        self.assertEqual(False, birth_before_death("2023-02-20", "1909-02-02"))
        self.assertEqual(False, birth_before_death("1989-05-20", "1809-02-02"))
        self.assertEqual(True, birth_before_death("1999-07-20", "NA"))
        
    
        
    
    
if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
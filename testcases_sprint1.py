#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:57:53 2018

@author: jackylee
"""

import unittest
from sprint1 import get_age, check_date, check_married, check_unique, birth_before_parent_death, check_gender


class Test_Get_age(unittest.TestCase):
    ''' get_age'''
    
    def test_alive(self):
        print("-------\nGet_age testing:")
        print("\nAlive testing:")
        self.assertEqual('24', get_age("1994-01-16"))
        self.assertNotEqual('22', get_age("1995-01-11"))
        self.assertNotEqual('0', get_age("1993-02-01"))
        print("Done")
        
    def test_dead(self):
        print("\nDead testing:")
        self.assertEqual('24', get_age("1920-02-26", "1944-09-01"))
        self.assertNotEqual('22', get_age("1995-01-21", "2000-09-20"))
        print("Done")
        
    def test_correct_date_age(self):
        print("\nCorrect date testing:")
        self.assertEqual('18', get_age("2000-02-29"))
        self.assertEqual('26', get_age("1992-02-28"))
        self.assertTrue(get_age("1992-02-28"))
        print("Done")
        
    def test_wrong_date_age(self):
        print("\nWrong date testing:")
        self.assertEqual("NA", get_age("1993-02-29"))
        self.assertEqual("NA", get_age("1992-03-32"))
        self.assertEqual("NA", get_age("1950-02-21","1990-09-32"))
        print("Done")
        
    def test_impossible_age(self):
        print("\nImpossible date testing:")
        self.assertEqual("NA", get_age("2020-02-20"))
        self.assertEqual("NA", get_age("1992-30-22"))
        self.assertEqual("NA", get_age("1978-02-40"))
        self.assertEqual("NA", get_age("1994-01-16","2020-02-20"))
        self.assertEqual("NA", get_age("1994-01-16","1992-30-22"))
        self.assertEqual("NA", get_age("1994-01-16","1978-02-40"))
        print("Done")

class Test_Check_date(unittest.TestCase):
    ''' check_date '''
    def test_correct_dates(self):
        print("-------\nCheck_date testing:")
        print("\nCorrect date testing:")
        self.assertTrue(check_date("2018-01-01"))
        self.assertTrue(check_date("1876-04-02"))
        self.assertTrue(check_date("1993-03-22"))
        self.assertEqual(False, check_date("2019-01-22"))
        print("Done")
    
    def test_wrong_dates(self):
        print("\nWrong date testing:")
        self.assertEqual(False, check_date("2018-01-32"))
        self.assertEqual(False, check_date("1987-02-30"))
        print("Done")
        
        
class Test_Check_married(unittest.TestCase):
    ''' check_married '''
    def test_correct_dates(self):
        print("-------\nCheck_married testing:")
        print("\nCorrect married testing:")
        self.assertTrue(check_married("1994-07-16","2018-02-10"))
        self.assertTrue(check_married("1834-01-26","1908-02-10"))
        self.assertTrue(check_married("1993-08-26","2012-02-28"))
        self.assertEqual(False, check_married("1976-07-16","1988-03-20"))
        self.assertEqual(False, check_married("1994-09-30","1965-04-02"))
        print("Done")
        
    def test_wrong_dates(self):
        print("\nWrong married testing:")
        self.assertEqual(False, check_married("1906-09-16","1988-03-40"))
        self.assertEqual(False, check_married("1994-09-30","1995-04-02"))
        self.assertEqual(False, check_married("1976-07-16","1968-03-20"))
        self.assertEqual(False, check_married("1994-09-30","1965-04-02"))
        self.assertEqual(False, check_married("1976-07-16","1988-04-40"))
        print("Done")
        
        
class Test_Birth_before_parent_death(unittest.TestCase):
    ''' birth_before_parent_death '''
    def test_correct_dates(self):
        print("-------\nBirth_before_parent_death testing:")
        print("\nCorrect birth testing:")
        self.assertTrue(birth_before_parent_death("1994-07-16","2018-02-10","2018-02-10"))
        self.assertTrue(birth_before_parent_death("1834-01-26","1908-02-10","2018-02-10"))
        self.assertTrue(birth_before_parent_death("1993-08-26","2012-02-28","2018-02-10"))
        self.assertEqual(True, birth_before_parent_death("1976-07-16","1988-03-20","2018-02-10"))
        self.assertEqual(False, birth_before_parent_death("1994-09-30","1965-04-02","2018-02-10"))
        print("Done")
        
    def test_wrong_dates(self):
        print("\nWrong birth testing:")
        self.assertEqual(False, birth_before_parent_death("1906-09-16","1988-03-40","2018-02-10"))
        self.assertEqual(False, birth_before_parent_death("1994-09-30","1993-04-02","2018-02-10"))
        self.assertEqual(False, birth_before_parent_death("1976-07-16","1968-03-20","2018-02-10"))
        self.assertEqual(False, birth_before_parent_death("1994-09-30","1965-04-02","2018-02-10"))
        self.assertEqual(False, birth_before_parent_death("1976-07-16","1988-04-40","2018-02-10"))
        print("Done")       
        
    
    
if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
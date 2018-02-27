# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:34:44 2018

@author: yujiezhong
"""

from Sprint1 import CmprDate
import unittest

class TestSprint1(unittest.TestCase):
    '''Test Sprint1.py'''
    
    def test_validbirth(self):
        self.assertTrue(CmprDate("1992-07-09","NA","NA"))
        self.assertTrue(CmprDate("1999-02-05","1999-03-15","NA"))
        self.assertTrue(CmprDate("1993-09-09","NA","1993-09-09"))
        self.assertTrue(CmprDate("2001-07-08","2002-09-10","2003-10-03"))
    
    def test_invalidbirth(self):
        self.assertFalse(CmprDate("1980-08-09","NA","1979-07-08"))
        self.assertFalse(CmprDate("1990-01-11","1989-02-01","NA"))
        self.assertFalse(CmprDate("1890-12-12","1890-02-08","1890-12-11"))
    
    def test_wrongdate(self):
        self.assertFalse(CmprDate("2019-13-33","NA","NA"))
        self.assertFalse(CmprDate("2018-03-24","NA","1990-09-02"))
        self.assertFalse(CmprDate("1998-02-30","1980-04-09","NA"))
    
    def test_wrongdayhusb(self):
        self.assertFalse(CmprDate("1998-09-10","1997-12-05","NA"))
        self.assertFalse(CmprDate("1909-01-02","1908-03-01","NA"))
        self.assertFalse(CmprDate("2000-03-08","1999-03-06","NA"))
    
    def test_wrongdaywife(self):
        self.assertFalse(CmprDate("1909-09-09","NA","1909-09-08"))
        self.assertFalse(CmprDate("1998-11-09","NA","1997-09-08"))
    
if __name__=="__main__":
    unittest.main()
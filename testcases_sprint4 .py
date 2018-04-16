#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:57:53 2018

@author: jackylee
"""

import unittest
from sprint4 import siblings, nieces_nephews, Siblings_Spacing, Multiple_Births


#testcases
# right dicts
indi_dict = {
        'I18': {'name': 'Haohao /Lee/ ', 'gender': 'M', 'dob': '1986-03-03', 'child': 'F3', 'death': 'NA', 'age': '32', 'alive': True, 'ID': 'I18', 'spouse': 'NA'},
        'I12': {'name': 'Sushi /Jan/ ', 'gender': 'M', 'dob': '1921-04-04', 'child': 'NA', 'death': 'NA', 'age': '97', 'alive': True, 'ID': 'I12', 'spouse': 'F7'}, 
        'I13': {'name': 'Fan /Luo/ ', 'gender': 'M', 'dob': '1917-03-03', 'child': 'NA', 'death': '1940-05-05', 'age': '23', 'alive': False, 'ID': 'I13', 'spouse': 'F8'}, 
        'I11': {'name': 'Tank /Lee/ ', 'gender': 'F', 'dob': '1920-04-03', 'child': 'F6', 'death': 'NA', 'age': '98', 'alive': True, 'ID': 'I11', 'spouse': 'F7'}, 
        'I3': {'name': 'Jack /Lee/ ', 'gender': 'M', 'dob': '1960-04-05', 'child': 'F4', 'death': 'NA', 'age': '58', 'alive': True, 'ID': 'I3', 'spouse': 'F3'}, 
        'I15': {'name': 'LS /Guo/ ', 'gender': 'M', 'dob': '1960-02-02', 'child': 'NA', 'death': 'NA', 'age': '58', 'alive': True, 'ID': 'I15', 'spouse': 'F5'}, 
        'I7': {'name': 'Lucy /Chan/ ', 'gender': 'F', 'dob': '1921-03-03', 'child': 'NA', 'death': 'NA', 'age': '97', 'alive': True, 'ID': 'I7', 'spouse': 'F4'}, 
        'I4': {'name': 'Yoyo /Lee/ ', 'gender': 'M', 'dob': '1990-02-06', 'child': 'F2', 'death': 'NA', 'age': '28', 'alive': True, 'ID': 'I4', 'spouse': 'NA'}, 
        'I8': {'name': 'Mody /Lee/ ', 'gender': 'M', 'dob': '1920-02-03', 'child': 'F6', 'death': 'NA', 'age': '98', 'alive': True, 'ID': 'I8', 'spouse': 'F4'}, 
        'I16': {'name': 'LH /Guan/ ', 'gender': 'F', 'dob': '1969-04-04', 'child': 'NA', 'death': 'NA', 'age': '49', 'alive': True, 'ID': 'I16', 'spouse': 'F5'}, 
        'I10': {'name': 'Ricky /Wei/ ', 'gender': 'F', 'dob': '1890-02-05', 'child': 'NA', 'death': '1968-04-06', 'age': '78', 'alive': False, 'ID': 'I10', 'spouse': 'F6'}, 
        'I6': {'name': 'Emma /Guo/ ', 'gender': 'F', 'dob': '1995-04-02', 'child': 'F5', 'death': 'NA', 'age': '23', 'alive': True, 'ID': 'I6', 'spouse': 'F1'}, 
        'I1': {'name': 'Jacky /Lee/ ', 'gender': 'M', 'dob': '1994-01-16', 'child': 'F2', 'death': 'NA', 'age': '24', 'alive': True, 'ID': 'I1', 'spouse': 'F1'}, 
        'I2': {'name': 'Sophie /Goo/ ', 'gender': 'F', 'dob': '1970-07-18', 'child': 'NA', 'death': 'NA', 'age': '48', 'alive': True, 'ID': 'I2', 'spouse': 'F2'}, 
        'I14': {'name': 'LiuLiu /Lee/ ', 'gender': 'F', 'dob': '1992-03-05', 'child': 'F2', 'death': 'NA', 'age': '26', 'alive': True, 'ID': 'I14', 'spouse': 'NA'}, 
        'I17': {'name': 'Zhazha /St/ ', 'gender': 'F', 'dob': '1964-04-04', 'child': 'NA', 'death': 'NA', 'age': '54', 'alive': True, 'ID': 'I17', 'spouse': 'F3'}, 
        'I5': {'name': 'CoCo /Lee/ ', 'gender': 'F', 'dob': '2015-06-09', 'child': 'F1', 'death': 'NA', 'age': '3', 'alive': True, 'ID': 'I5', 'spouse': 'NA'}, 
        'I9': {'name': 'Mike /Lee/ ', 'gender': 'M', 'dob': '1890-02-02', 'child': 'NA', 'death': '1970-06-08', 'age': '80', 'alive': False, 'ID': 'I9', 'spouse': 'F6'},
        }

fam_dict = {
        'F8': {'wife_name': 'Tank /Lee/ ', 'divorced': 'NA', 'wife_id': 'I11', 'married': '1938-05-05', 'children': set(), 'husb_id': 'I13', 'ID': 'F8', 'husb_name': 'Fan /Luo/ '}, 
        'F2': {'wife_name': 'Sophie /Goo/ ', 'divorced': 'NA', 'wife_id': 'I2', 'married': '1988-06-18', 'children': {'I1', 'I4', 'I14'}, 'husb_id': 'I3', 'ID': 'F2', 'husb_name': 'Jack /Lee/ '},
        'F5': {'wife_name': 'LH /Guan/ ', 'divorced': 'NA', 'wife_id': 'I16', 'married': '1992-12-12', 'children': {'I6'}, 'husb_id': 'I15', 'ID': 'F5', 'husb_name': 'LS /Guo/ '}, 
        'F7': {'wife_name': 'Tank /Lee/ ', 'divorced': 'NA', 'wife_id': 'I11', 'married': '1950-05-14', 'children': set(), 'husb_id': 'I12', 'ID': 'F7', 'husb_name': 'Sushi /Jan/ '}, 
        'F3': {'wife_name': 'Zhazha /St/ ', 'divorced': '1987-08-08', 'wife_id': 'I17', 'married': '1983-07-07', 'children': {'I18'}, 'husb_id': 'I3', 'ID': 'F3', 'husb_name': 'Jack /Lee/ '}, 
        'F6': {'wife_name': 'Ricky /Wei/ ', 'divorced': 'NA', 'wife_id': 'I10', 'married': '1915-10-10', 'children': {'I8', 'I11'}, 'husb_id': 'I9', 'ID': 'F6', 'husb_name': 'Mike /Lee/ '}, 
        'F1': {'wife_name': 'Emma /Guo/ ', 'divorced': '2017-05-10', 'wife_id': 'I6', 'married': '2013-04-04', 'children': {'I5'}, 'husb_id': 'I1', 'ID': 'F1', 'husb_name': 'Jacky /Lee/ '}, 
        'F4': {'wife_name': 'Lucy /Chan/ ', 'divorced': 'NA', 'wife_id': 'I7', 'married': '1955-11-11', 'children': {'I3'}, 'husb_id': 'I8', 'ID': 'F4', 'husb_name': 'Mody /Lee/ '},
        }
# wrong cases for sibilings spacing
indi_dict1 = {
        'I1': {'dob': '1990-06-02'}, 
        'I2':{'dob':'1990-09-09'},
        }
fam_dict1 = {
        'F1':{'children': {'I1','I2'}},
        }
# wrong cases for multiple births
indi_dict2 = {
        'I1':{'dob': '1990-09-09'},
        'I2':{'dob': '1990-09-09'},
        'I3':{'dob': '1990-09-09'},
        'I4':{'dob': '1990-09-09'},
        'I5':{'dob': '1990-09-09'},
        'I6':{'dob': '1990-09-09'},
        'I7':{'dob': '1969-09-09'},
        'I8':{'dob': '1968-08-08'},
        }
fam_dict2 = {
        'F1':{'children':{'I1','I2','I3','I4','I5','I6'}},
        }


class TestSprint4(unittest.TestCase):
    
    def test_SiblingsSpacing(self):
        self.assertTrue(Siblings_Spacing(fam_dict['F1'], indi_dict))
        self.assertFalse(Siblings_Spacing(fam_dict1['F1'], indi_dict1))
        
    def test_MultipleBirths(self):
        self.assertTrue(Multiple_Births(fam_dict['F2'], indi_dict))
        self.assertFalse(Multiple_Births(fam_dict2['F1'], indi_dict2))
        
    def test_siblings_marr(self):
        flag, fam = siblings("I1", fam_dict['F1'], fam_dict)
        self.assertTrue(flag)
        self.assertEqual(None, fam)
        
    def test_aunt_uncle_marr(self):
        self.assertTrue(nieces_nephews('I1', "I6", fam_dict))

if __name__=='__main__':
    unittest.main()
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 19:19:31 2018

@author: yujiezhong
"""
import datetime,unittest
NOW = datetime.datetime.now()


def List_Deceased(indi_dict):
    deadlst = []
    for key in indi_dict:
        if indi_dict[key]['death'] != "NA":
            deadlst.append(key)
    return deadlst

def List_Recent_Birth(indi_dict):
    birthlst = []
    for key in indi_dict:
        birthdate = datetime.datetime.strptime(indi_dict[key]['dob'],'%Y-%m-%d')
        if 0 <= (NOW - birthdate).days <= 30:
            birthlst.append(key)
    return birthlst


#testcase

indi_dict = {'I20': {'dob': '2018-03-16','death': 'NA'},'I18': {'name': 'Haohao /Lee/ ', 'gender': 'M', 'dob': '1986-03-03', 'child': 'F3', 'death': 'NA', 'age': '32', 'alive': True, 'ID': 'I18', 'spouse': 'NA'}, 'I12': {'name': 'Sushi /Jan/ ', 'gender': 'M', 'dob': '1921-04-04', 'child': 'NA', 'death': 'NA', 'age': '97', 'alive': True, 'ID': 'I12', 'spouse': 'F7'}, 'I13': {'name': 'Fan /Luo/ ', 'gender': 'M', 'dob': '1917-03-03', 'child': 'NA', 'death': '1940-05-05', 'age': '23', 'alive': False, 'ID': 'I13', 'spouse': 'F8'}, 'I11': {'name': 'Tank /Lee/ ', 'gender': 'F', 'dob': '1920-04-03', 'child': 'F6', 'death': 'NA', 'age': '98', 'alive': True, 'ID': 'I11', 'spouse': 'F7'}, 'I3': {'name': 'Jack /Lee/ ', 'gender': 'M', 'dob': '1960-04-05', 'child': 'F4', 'death': 'NA', 'age': '58', 'alive': True, 'ID': 'I3', 'spouse': 'F3'}, 'I15': {'name': 'LS /Guo/ ', 'gender': 'M', 'dob': '1960-02-02', 'child': 'NA', 'death': 'NA', 'age': '58', 'alive': True, 'ID': 'I15', 'spouse': 'F5'}, 'I7': {'name': 'Lucy /Chan/ ', 'gender': 'F', 'dob': '1921-03-03', 'child': 'NA', 'death': 'NA', 'age': '97', 'alive': True, 'ID': 'I7', 'spouse': 'F4'}, 'I4': {'name': 'Yoyo /Lee/ ', 'gender': 'M', 'dob': '1990-02-06', 'child': 'F2', 'death': 'NA', 'age': '28', 'alive': True, 'ID': 'I4', 'spouse': 'NA'}, 'I8': {'name': 'Mody /Lee/ ', 'gender': 'M', 'dob': '1920-02-03', 'child': 'F6', 'death': 'NA', 'age': '98', 'alive': True, 'ID': 'I8', 'spouse': 'F4'}, 'I16': {'name': 'LH /Guan/ ', 'gender': 'F', 'dob': '1969-04-04', 'child': 'NA', 'death': 'NA', 'age': '49', 'alive': True, 'ID': 'I16', 'spouse': 'F5'}, 'I10': {'name': 'Ricky /Wei/ ', 'gender': 'F', 'dob': '1890-02-05', 'child': 'NA', 'death': '1968-04-06', 'age': '78', 'alive': False, 'ID': 'I10', 'spouse': 'F6'}, 'I6': {'name': 'Emma /Guo/ ', 'gender': 'F', 'dob': '1995-04-02', 'child': 'F5', 'death': 'NA', 'age': '23', 'alive': True, 'ID': 'I6', 'spouse': 'F1'}, 'I1': {'name': 'Jacky /Lee/ ', 'gender': 'M', 'dob': '1994-01-16', 'child': 'F2', 'death': 'NA', 'age': '24', 'alive': True, 'ID': 'I1', 'spouse': 'F1'}, 'I2': {'name': 'Sophie /Goo/ ', 'gender': 'F', 'dob': '1970-07-18', 'child': 'NA', 'death': 'NA', 'age': '48', 'alive': True, 'ID': 'I2', 'spouse': 'F2'}, 'I14': {'name': 'LiuLiu /Lee/ ', 'gender': 'F', 'dob': '1992-03-05', 'child': 'F2', 'death': 'NA', 'age': '26', 'alive': True, 'ID': 'I14', 'spouse': 'NA'}, 'I17': {'name': 'Zhazha /St/ ', 'gender': 'F', 'dob': '1964-04-04', 'child': 'NA', 'death': 'NA', 'age': '54', 'alive': True, 'ID': 'I17', 'spouse': 'F3'}, 'I5': {'name': 'CoCo /Lee/ ', 'gender': 'F', 'dob': '2015-06-09', 'child': 'F1', 'death': 'NA', 'age': '3', 'alive': True, 'ID': 'I5', 'spouse': 'NA'}, 'I9': {'name': 'Mike /Lee/ ', 'gender': 'M', 'dob': '1890-02-02', 'child': 'NA', 'death': '1970-06-08', 'age': '80', 'alive': False, 'ID': 'I9', 'spouse': 'F6'}}

class TestSprint1(unittest.TestCase):
    
    def test_ListDeceased(self):
        self.assertEqual(List_Deceased(indi_dict),['I13', 'I10', 'I9'])
    
    def test_ListRecentBirth(self):
        self.assertEqual(List_Recent_Birth(indi_dict), ['I20'])
    
    
    
if __name__=="__main__":
    unittest.main()
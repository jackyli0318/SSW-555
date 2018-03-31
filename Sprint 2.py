# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:19:21 2018

@author: yujiezhong
"""
import unittest

    
def No_Marriage_To_Descendants(ID,fam_dict):
    # ID is family id, fam_dict is family dictionary
    husb_id = fam_dict[ID]['husb_id']
    wife_id = fam_dict[ID]['wife_id']
    descendants = []
    find_descendants(ID,fam_dict,descendants)
    if husb_id in descendants or wife_id in descendants:
        return False
    return True
        
        
def find_descendants(ID,fam_dict,desc):
    desc.extend(fam_dict[ID]['children'])
    for key in fam_dict:
        if key != ID:
            if fam_dict[key]['husb_id']in fam_dict[ID]['children'] or fam_dict[key]['wife_id'] in fam_dict[ID]['children']:
                find_descendants(key,fam_dict,desc)
        else:
            continue
        

def Unique_Name_N_Birth(ID1,ID2,indi_dict):    
    name1 = indi_dict[ID1]['name']
    name2 = indi_dict[ID2]['name']
    birt1 = indi_dict[ID1]['dob']
    birt2 = indi_dict[ID2]['dob']
    
    if name1 == name2 and birt1 == birt2:
        indi_dict.pop(ID2)
        return False
    else:
        return True
        


#unittest

# family record
fam_dict1 = {'F1': {'children': ['I13','I2','I3'], 'husb_id': 'I1', 'wife_id': 'I14'}, 'F2': {'children': ['I5', 'I10', 'I12'], 'husb_id': 'I2', 'wife_id': 'I5'}}
fam_dict = {'F8': {'wife_name': 'Tank /Lee/ ', 'divorced': 'NA', 'wife_id': 'I11', 'married': '1938-05-05', 'children': [], 'husb_id': 'I13', 'ID': 'F8', 'husb_name': 'Fan /Luo/ '}, 'F2': {'wife_name': 'Sophie /Goo/ ', 'divorced': 'NA', 'wife_id': 'I2', 'married': '1988-06-18', 'children': ['I1', 'I4', 'I14'], 'husb_id': 'I3', 'ID': 'F2', 'husb_name': 'Jack /Lee/ '}, 'F5': {'wife_name': 'LH /Guan/ ', 'divorced': 'NA', 'wife_id': 'I16', 'married': '1992-12-12', 'children': ['I6'], 'husb_id': 'I15', 'ID': 'F5', 'husb_name': 'LS /Guo/ '}, 'F7': {'wife_name': 'Tank /Lee/ ', 'divorced': 'NA', 'wife_id': 'I11', 'married': '1950-05-14', 'children': [], 'husb_id': 'I12', 'ID': 'F7', 'husb_name': 'Sushi /Jan/ '}, 'F3': {'wife_name': 'Zhazha /St/ ', 'divorced': '1987-08-08', 'wife_id': 'I17', 'married': '1983-07-07', 'children': ['I18'], 'husb_id': 'I3', 'ID': 'F3', 'husb_name': 'Jack /Lee/ '}, 'F6': {'wife_name': 'Ricky /Wei/ ', 'divorced': 'NA', 'wife_id': 'I10', 'married': '1915-10-10', 'children': ['I8', 'I11'], 'husb_id': 'I9', 'ID': 'F6', 'husb_name': 'Mike /Lee/ '}, 'F1': {'wife_name': 'Emma /Guo/ ', 'divorced': '2017-05-10', 'wife_id': 'I6', 'married': '2013-04-04', 'children': ['I5'], 'husb_id': 'I1', 'ID': 'F1', 'husb_name': 'Jacky /Lee/ '}, 'F4': {'wife_name': 'Lucy /Chan/ ', 'divorced': 'NA', 'wife_id': 'I7', 'married': '1955-11-11', 'children': ['I3'], 'husb_id': 'I8', 'ID': 'F4', 'husb_name': 'Mody /Lee/ '}}
# different name and different birth
indi_dict1 = {'I18': {'name': 'Haohao /Lee/ ', 'gender': 'M', 'dob': '1986-03-03', 'child': "{'F3'}", 'death': 'NA', 'age': '32', 'alive': True, 'ID': 'I18', 'spouse': 'NA'}, 'I12': {'name': 'Sushi /Jan/ ', 'gender': 'M', 'dob': '1921-04-04', 'child': 'NA', 'death': 'NA', 'age': '97', 'alive': True, 'ID': 'I12', 'spouse': "{'F7'}"}}
# same name and same birth
indi_dict2 = {'I18': {'name': 'Haohao /Lee/ ', 'gender': 'M', 'dob': '1986-03-03', 'child': "{'F3'}", 'death': 'NA', 'age': '32', 'alive': True, 'ID': 'I18', 'spouse': 'NA'}, 'I12': {'name': 'Haohao /Lee/ ', 'gender': 'M', 'dob': '1986-03-03', 'child': 'NA', 'death': 'NA', 'age': '97', 'alive': True, 'ID': 'I12', 'spouse': "{'F7'}"}}
# same name and different birth
indi_dict3 = {'I18': {'name': 'Haohao /Lee/ ', 'gender': 'M', 'dob': '1986-03-03', 'child': "{'F3'}", 'death': 'NA', 'age': '32', 'alive': True, 'ID': 'I18', 'spouse': 'NA'}, 'I12': {'name': 'Haohao /Lee/ ', 'gender': 'M', 'dob': '1985-03-03', 'child': 'NA', 'death': 'NA', 'age': '97', 'alive': True, 'ID': 'I12', 'spouse': "{'F7'}"}}
# different name and same birth
indi_dict4 = {'I18': {'name': 'Haohao /Lee/ ', 'gender': 'M', 'dob': '1986-03-03', 'child': "{'F3'}", 'death': 'NA', 'age': '32', 'alive': True, 'ID': 'I18', 'spouse': 'NA'}, 'I12': {'name': 'Sushi /Jan/ ', 'gender': 'M', 'dob': '1986-03-03', 'child': 'NA', 'death': 'NA', 'age': '97', 'alive': True, 'ID': 'I12', 'spouse': "{'F7'}"}}

class TestSprint1(unittest.TestCase):
    '''Test Sprint1.py'''
    
    def test_NoMarrToDesc(self):
        self.assertTrue(No_Marriage_To_Descendants('F6',fam_dict))
        self.assertTrue(No_Marriage_To_Descendants('F8',fam_dict))
        self.assertTrue(No_Marriage_To_Descendants('F5',fam_dict))
        self.assertTrue(No_Marriage_To_Descendants('F7',fam_dict))
        self.assertFalse(No_Marriage_To_Descendants('F2',fam_dict1))
    
    def test_UniqNameNBirt(self):
        self.assertTrue(Unique_Name_N_Birth('I18','I12', indi_dict1))
        self.assertFalse(Unique_Name_N_Birth('I18','I12', indi_dict2))
        self.assertTrue(Unique_Name_N_Birth('I18','I12', indi_dict3))
        self.assertTrue(Unique_Name_N_Birth('I18','I12', indi_dict4))
    
    
    
if __name__=="__main__":
    unittest.main()


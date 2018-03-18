# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:19:21 2018

@author: yujiezhong
"""
    
    
def No_Marriage_To_Descendants(fam_dict):
    for key in fam_dict:
        husb_id = fam_dict[key]['husb_id']
        wife_id = fam_dict[key]['wife_id']
        children = fam_dict[key]['children']
        if husb_id in children or wife_id in children:
            return False
        return True
        

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
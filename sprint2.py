#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 22:28:03 2018

@author: jackylee
"""
import datetime


# US40
def set_line_num(tmp_dict, field, line_num):
    tmp_dict['line_dict'][field] = line_num
    return tmp_dict


def get_line_num(tmp_dict, field):
    return tmp_dict.get('line_dict').get(field, 'NA')


# US04
def marr_before_div(tmp_fam):
    marr = tmp_fam.get('married')
    div = tmp_fam.get('divorced')
    flag = False
    
    if marr != 'NA':
        marr = datetime.datetime.strptime(marr,"%Y-%m-%d")
    if div != "NA":
        div = datetime.datetime.strptime(div,"%Y-%m-%d")

    if div == "NA":
        flag = True
    if marr != "NA" and div != "NA":
        if marr < div:
            flag = True
        else:
            flag = False
    
    return flag


# US17
#def no_marriage_to_descendants(tmp_fam):
#    husb_id = tmp_fam['husb_id']
#    wife_id = tmp_fam['wife_id']
#    children = tmp_fam['children']
#    if husb_id in children or wife_id in children:
#        return False
#    return True


     
#desc = []
#fam_dict = {
#        'F1': {"ID": "F1", "children": ['I15', 'I14', 'I2', 'I3'], 'husb_id':'I13', 'wife_id': 'I16'},
#        'F2': {"ID": "F2", "children": ['I17', 'I8', 'I9'], 'husb_id':'I15', 'wife_id': 'I14'},
#        'F3': {"ID": "F3", "children": ['I10', 'I22'], 'husb_id':'I8', 'wife_id': 'I9'},
#        'F4': {"ID": "F4", "children": ['I26'], 'husb_id':'I11', 'wife_id': 'I22'},
#        'F5': {"ID": "F5", "children": ['I16'], 'husb_id':'I26', 'wife_id': 'I32'},
#        }
#tmp_fam = {"ID": "F1", "children": ['I15', 'I14', 'I2', 'I3'], 'husb_id':'I13', 'wife_id': 'I16'}
     
# US17   
def no_marriage_to_descendants(tmp_fam,fam_dict):
    # ID is family id, fam_dict is family dictionary
    husb_id = tmp_fam['husb_id']
    wife_id = tmp_fam['wife_id']
    desc = list()
    desc.extend(tmp_fam['children'])
    if husb_id in desc or wife_id in desc:
        # if in return False
        return False
    
    already_fams = set()
    already_fams.add(tmp_fam["ID"])
    
    flag = True
    while(flag):
        flag = False
        # iterate all families
        for key in fam_dict:
            # skip already extended families
            if key in already_fams:
                continue
            # if husb or wife in desc, extend their children
            if fam_dict[key]['husb_id'] in desc or fam_dict[key]['wife_id'] in desc:
                desc.extend(fam_dict[key]['children'])
                flag = True
                already_fams.add(key)
                # iterate all families again
                break
            
    if husb_id in desc or wife_id in desc:
        # if in return False
        return False
    else:
        return True
        
        

        

# US23
def unique_name_birth(INDI_SET,tmp_indi):    
    tmp_name_birth = (tmp_indi['name'], tmp_indi['dob'])
    if tmp_name_birth in INDI_SET:
        return False, INDI_SET
    
    INDI_SET.add(tmp_name_birth)
    return True, INDI_SET
    
    
# US07
def check_150(age):
    if int(age)>150:
        age = "NA"
    return age


# US06
def div_before_death(indi_dict, div_date, husb_id, wife_id):
    div_date = datetime.datetime.strptime(div_date,"%Y-%m-%d")
    husb_deat = indi_dict[husb_id].get("death")
    wife_deat = indi_dict[wife_id].get("death")
    
    husb_flag = False
    wife_flag = False
    
    if husb_deat=='NA' and wife_deat=='NA':
        return True, ""
    
    if husb_deat!='NA':
        husb_deat = datetime.datetime.strptime(husb_deat,"%Y-%m-%d")
        if husb_deat > div_date:
            husb_flag = True
            
    if wife_deat!='NA':
        wife_deat = datetime.datetime.strptime(wife_deat,"%Y-%m-%d")
        if wife_deat > div_date:
            wife_flag = True
    
    if husb_flag and wife_flag:
        return True, ""
    elif husb_flag:
        return False, "hs"
    elif wife_flag:
        return False, "wf"
    else:
        return False, "hs_wf"
        
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
def no_marriage_to_descendants(tmp_fam):
    husb_id = tmp_fam['husb_id']
    wife_id = tmp_fam['wife_id']
    children = tmp_fam['children']
    if husb_id in children or wife_id in children:
        return False
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
        
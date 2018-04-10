#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

NOW = datetime.datetime.now()


#US 03
def birth_before_death(birth,death):
    #birth year, month and day
    '''
    if birth!="NA":
        if check_date(birth)==True:
            birthdate = datetime.datetime.strptime(birth,"%Y-%m-%d")
        else:
            return False
    #death year, month and day
    if death!="NA":
        if check_date(death)==True:
            deathdate = datetime.datetime.strptime(death,"%Y-%m-%d")
        else:
            return False
        '''
    #make comparison
    if (birth!="NA" and death=="NA"):
        return True
    elif (birth=="NA" and death=="NA"):
        return True
    elif (birth!="NA" and death!="NA"):
        birthdate = datetime.datetime.strptime(birth,"%Y-%m-%d")
        deathdate = datetime.datetime.strptime(death,"%Y-%m-%d")
        if (deathdate-birthdate).days >= 0:
            return True
        else:
            return False
    else:
        return False

#US 05
def marr_before_death(indi_dict, marr_date, husb_id, wife_id):
    marr_date = datetime.datetime.strptime(marr_date,"%Y-%m-%d")
    husb_deat = indi_dict[husb_id].get("death")
    wife_deat = indi_dict[wife_id].get("death")
    
    husb_flag = False
    wife_flag = False
    
    if husb_deat=='NA' and wife_deat=='NA':
        return True, ""
    
    if husb_deat!='NA':
        husb_deat = datetime.datetime.strptime(husb_deat,"%Y-%m-%d")
        if husb_deat > marr_date:
            husb_flag = True
    else:
        husb_flag = True
            
    if wife_deat!='NA':
        wife_deat = datetime.datetime.strptime(wife_deat,"%Y-%m-%d")
        if wife_deat > marr_date:
            wife_flag = True
    else:
        wife_flag = True
    
    if husb_flag and wife_flag:
        return True, ""
    elif husb_flag:
        return False, "wf"
    elif wife_flag:
        return False, "hs"
    else:
        return False, "hs_wf"
    
# US30
def get_married_lst(fam, marr_lst):
    if fam['divorced'] == 'NA' and fam['married']!="NA":
        marr_lst.append(fam['husb_id'])
        marr_lst.append(fam['wife_id'])
    return marr_lst

def get_living_lst(living_lst, indi_dict):
    for indi_id in living_lst:
        tmp_indi = indi_dict[indi_id]
        # or 
        # if tmp_indi['alive'] == False:
        if tmp_indi['death'] != 'NA' or tmp_indi['dob'] == "NA":
            living_lst.remove(indi_id)
    return living_lst


# US31
def get_single_lst(indi_dict, marr_lst):
    single_lst = list()
    for indi_id in indi_dict:
        tmp_indi = indi_dict[indi_id]
        if indi_id in marr_lst:
            continue
        else:
            # if tmp_indi['alive'] == False:
            if tmp_indi['death'] == 'NA' and tmp_indi['dob'] != "NA":
                single_lst.append(indi_id)
    return single_lst


# US29
def list_deceased(tmp_indi, deceased_lst):
    if tmp_indi['death'] != "NA":
        deceased_lst.append(tmp_indi['ID'])
    return deceased_lst


# US37
def list_recent_birth(tmp_indi, birth_lst):
    try:
        birthdate = datetime.datetime.strptime(tmp_indi['dob'],'%Y-%m-%d')
    except ValueError:
        return birth_lst
    if 0 <= (NOW - birthdate).days <= 30:
        birth_lst.append(tmp_indi['ID'])
    return birth_lst








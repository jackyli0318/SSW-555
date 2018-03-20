#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

#US 03
def birth_before_death(birth,death):
	#birth year, month and day
	if birth!="NA":
        if check_date(birth)==True:
            birthdate = datetime.datetime.strptime(cbirth,"%Y-%m-%d")
        else:
            return False
    #death year, month and day
	if death!="NA":
        if check_date(death)==True:
            deathdate = datetime.datetime.strptime(cbirth,"%Y-%m-%d")
        else:
            return False
    #make comparison
    if (birthdate!="NA" and deathdate=="NA"):
    	return True
    elif (birthdate!="NA" and deathdate!="NA"):
    	if (deathdate-birthdate).days >= 0:
    		return True
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
            
    if wife_deat!='NA':
        wife_deat = datetime.datetime.strptime(wife_deat,"%Y-%m-%d")
        if wife_deat > marr_date:
            wife_flag = True
    
    if husb_flag and wife_flag:
        return True, ""
    elif husb_flag:
        return False, "hs"
    elif wife_flag:
        return False, "wf"
    else:
        return False, "hs_wf"
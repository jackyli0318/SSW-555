#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:01:58 2018

@author: jackylee
"""
import datetime

NOW = datetime.datetime.now().strftime('%Y-%m-%d')
NOW_YEAR = datetime.datetime.now().strftime('%Y')
NOW_MONTH = datetime.datetime.now().strftime('%m')
NOW_DAY = datetime.datetime.now().strftime('%d')

#US42, US01
def check_date(date):
    try:
        if datetime.datetime.strptime(date,"%Y-%m-%d") > datetime.datetime.now():
#            print(date,"is an impossible date!")
            return False
    except ValueError:
#        print(date,"is an impossible date!")
        return [False,"42"]
    return True

#US10, US02
#birth before married & married after 14
def check_married(birth,marr):
    if check_date(birth)!=True or check_date(marr)!=True:
        return False
    marrdate = datetime.datetime.strptime(marr,"%Y-%m-%d")
    birthdate = datetime.datetime.strptime(birth,"%Y-%m-%d")
    
    if birthdate > marrdate:
#        print("Marriage should not occur before birth!")
        return False
#    else:
#        return True
    marrage = marrdate.year - birthdate.year
    if birthdate.month > marrdate.month:
        marrage -= 1
    elif birthdate.month == marrdate.month:
        if birthdate.day > marrdate.day:
            marrage -= 1
    
    if marrage < 14:
#        print("Marriage should occur after 14 years old!")
        return [False,"10"]
    else:
        return True
        

def get_age(start, end=NOW):
    if check_date(start)!=True or check_date(end)!=True:
        age = "NA"
        return age
    else:
        startdate = datetime.datetime.strptime(start,"%Y-%m-%d")
        enddate = datetime.datetime.strptime(end,"%Y-%m-%d")
        if startdate > enddate:
            age = "NA"
#            print("Birth should occur before death!")
            return age
        age = enddate.year - startdate.year
        if startdate.month > enddate.month:
            age -= 1
        elif startdate.month == enddate.month:
            if startdate.day > enddate.day:
                age -= 1
        return str(age)


def check_unique(SET, ID):
    if ID in SET:
#        print("ID:"+ ID +" exists! It is not unique!")
        return False, SET
    else:
        SET.add(ID)
        return True, SET
    

def birth_before_parent_death(cbirth,hdeath,wdeath):
    #children birth year, month and day
    if cbirth != "NA":
        if check_date(cbirth)==True:
            cbirthdate = datetime.datetime.strptime(cbirth,"%Y-%m-%d")
        else:
            return False
            
    #husband death year, month and day
    if hdeath != "NA":
        if check_date(hdeath)==True:
            hdeathdate = datetime.datetime.strptime(hdeath,"%Y-%m-%d")
        else:
            return False
            
    #wife death year, month and day
    if wdeath != "NA":
        if check_date(wdeath)==True:
            wdeathdate = datetime.datetime.strptime(wdeath,"%Y-%m-%d")
        else:
            return False

    #compare dates
    if (hdeath == "NA" and wdeath == "NA"):
        return True
    elif (hdeath == "NA" and wdeath != "NA"):
        if (wdeathdate-cbirthdate).days>=0:
            return True
    elif (hdeath != "NA" and wdeath == "NA"):
        if (cbirthdate-hdeathdate).days<=270:
            return True
    elif (hdeath != "NA" and wdeath != "NA"):
        if (wdeathdate-cbirthdate).days>=0 and (cbirthdate-hdeathdate).days<=270:
            return True
        else:
            return False
    else: 
        return False
   

def check_gender(ID,fam_dict,indi_dict):
    
    husb_id = fam_dict[ID]['husb_id']
    wife_id = fam_dict[ID]['wife_id']
    
    if indi_dict[husb_id]['gender']=="M" and indi_dict[wife_id]['gender']=="F":
        return True, ""
    elif indi_dict[husb_id]['gender']!="M":
        return False, husb_id
    else:
        return False, wife_id
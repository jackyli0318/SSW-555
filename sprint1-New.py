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


def check_date(date):
    try:
        if datetime.datetime.strptime(date,"%Y-%m-%d") > datetime.datetime.now():
            print(date,"is an impossible date!")
            return False
    except ValueError:
        print(date,"is an impossible date!")
        return False
    return True


def check_married(birth,marr):
    marrdate = datetime.datetime.strptime(marr,"%Y-%m-%d")
    birthdate = datetime.datetime.strptime(birth,"%Y-%m-%d")
    
    marrage = marrdate.year - birthdate.year
    if birthdate.month > marrdate.month:
        marrage -= 1
    elif birthdate.month == marrdate.month:
        if birthdate.day > marrdate.day:
            marrage -= 1
    
    if marrage < 14:
        return False
    else:
        return True
        

def get_age(start):
    end = NOW
    if check_date(start)==False:
        age = "NA"
        return age
    else:
        startdate = datetime.datetime.strptime(start,"%Y-%m-%d")
        enddate = datetime.datetime.strptime(end,"%Y-%m-%d")
        age = enddate.year - startdate.year
        if startdate.month > enddate.month:
            age -= 1
        elif startdate.month == enddate.month:
            if startdate.day > enddate.day:
                age -= 1
        return age


def check_unique(SET, ID):
    if ID in SET:
        return False, SET
    else:
        SET.add(ID)
        return True, SET
    

def Birth_Before_Parent_Death(cbirth,hdeath,wdeath):
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
   

def Check_Gender(ID,fam_dict,indi_dict):
    husb_id = fam_dict[ID]['husb_id']
    wife_id = fam_dict[ID]['wife_id']
    
    if indi_dict[husb_id]['gender']=="M" and indi_dict[wife_id]['gender']=="F":
        return True
    else:
        return False
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:33:20 2018

@author: yujiezhong
"""
import datetime


def check_date(date):
    try:
        if datetime.datetime.strptime(date,"%Y-%m-%d") > datetime.datetime.now():
            print(date,"is an impossible date!")
            return False
    except ValueError:
        print(date,"is an impossible date!")
        return False
    return True


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
   

def Check_Gender(fam_id,fam_dict,indi_dict):
    husb_id = fam_dict[fam_id]['husb_id']
    wife_id = fam_dict[fam_id]['wife_id']
    
    if indi_dict[husb_id]['gender']=="M" and indi_dict[wife_id]['gender']=="F":
        return True
    else:
        return False
    
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:19:21 2018

@author: yujiezhong
"""
import datetime


def Marriage_Before_Death(marr,hdeath,wdeath):
    #marriage date
    marrdate = datetime.datetime.strptime(marr,"%Y-%m-%d")
    #husband death date
    if hdeath != "NA":
        hdeathdate = datetime.datetime.strptime(hdeath,"%Y-%m-%d")
    #wife death date
    if wdeath != "NA":
        wdeathdate = datetime.datetime.strptime(wdeath,"%Y-%m-%d")
    
    if hdeath == "NA" and wdeath == "NA":
        return True
    elif hdeath == "NA" and wdeath != "NA":
        if (wdeathdate - marrdate).days > 0:
            return True
    elif hdeath != "NA" and wdeath == "NA":
        if (hdeathdate - marrdate).days > 0:
            return True
    elif hdeath != "NA" and wdeath != "NA":
        if (wdeathdate - marrdate).days > 0 and (hdeathdate - marrdate).days > 0:
            return True
    else:
        return False
        

def Unique_Name_N_Birth(ID1,ID2,indi_dict):    
    name1 = indi_dict[ID1]['name']
    name2 = indi_dict[ID2]['name']
    birt1 = indi_dict[ID1]['dob']
    birt2 = indi_dict[ID2]['dob']
    
    if name1 == name2 and birt1 == birt2:
        del indi_dict[ID2]
        return False
    else:
        return True
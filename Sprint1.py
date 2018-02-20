# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:33:20 2018

@author: yujiezhong
"""
def CheckDate(date):
    day30 = ['04','06','09','11']
    day31 = ['01','03','05','07','08','10','12']
    if len(date) == 8:
        if int(date) <= 20180219:
            if date[4:6] in day30:
                if int(date[6:])<=30:
                    return True
                else:
                    return False
            elif date[4:6] in day31:
                if int(date[6:])<=31:
                    return True
                else:
                    return False
            elif date[4:6] == "02":
                if int(date[6:])<=28:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def CmprDate(cbirth,hdeath,wdeath):
    cbirthdate = "".join(cbirth.split("-"))# Children's birthday
    hdeathdate = "".join(hdeath.split("-"))# Husband death date
    wdeathdate = "".join(wdeath.split("-"))# Wife death date

    if (hdeath == "NA" and wdeath == "NA"):
        if CheckDate(cbirthdate)==True:
            return True
        else:
            return False
    elif (hdeath == "NA" and wdeath != "NA"):
        if CheckDate(cbirthdate)==True and CheckDate(wdeathdate)==True:
            if int(cbirthdate) <= int(wdeathdate):
                return True
            else:
                return False
        else: 
            return False
    elif (hdeath != "NA" and wdeath == "NA"):
        if CheckDate(cbirthdate)==True and CheckDate(hdeathdate)==True:
            if int(hdeathdate[:4]) > int(cbirthdate[:4]):
                return True
            elif hdeathdate[:4] == cbirthdate[:4]: #if husband death year equals to child birth year
                if int(cbirthdate[4:6])-int(hdeathdate[4:6])<9:
                    return True
                elif int(cbirthdate[4:6])-int(hdeathdate[4:6])==9:
                    if int(cbirthdate[6:])-int(hdeathdate[6:])<=0:
                        return True
                    else:
                        return False
                else:
                    return False
            elif int(hdeathdate[:4])+1 == int(cbirthdate[:4]): #if husband death year is 1 year earlier than child birth year
                if 12-int(hdeathdate[4:6])+int(cbirthdate[4:6])<9:
                    return True
                elif 12-int(hdeathdate[4:6])+int(cbirthdate[4:6])==9:
                    if int(cbirthdate[6:])-int(hdeathdate[6:])<=0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif (hdeath != "NA" and wdeath != "NA"):
        if CheckDate(cbirthdate)==True and CheckDate(hdeathdate)==True and CheckDate(wdeathdate)==True:
            if int(cbirthdate) <= int(wdeathdate):
                if int(hdeathdate[:4]) > int(cbirthdate[:4]):
                    return True
                elif hdeathdate[:4] == cbirthdate[:4]: 
                    if int(cbirthdate[4:6])-int(hdeathdate[4:6])<9:
                        return True
                    elif int(cbirthdate[4:6])-int(hdeathdate[4:6])==9:
                        if int(cbirthdate[6:])-int(hdeathdate[6:])<=0:
                            return True
                        else:
                            return False
                    else:
                        return False
                elif int(hdeathdate[:4])+1 == int(cbirthdate[:4]):
                    if 12-int(hdeathdate[4:6])+int(cbirthdate[4:6])<9:
                        return True
                    elif 12-int(hdeathdate[4:6])+int(cbirthdate[4:6])==9:
                        if int(cbirthdate[6:])-int(hdeathdate[6:])<=0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else: 
            return False
    else:
        return False


        
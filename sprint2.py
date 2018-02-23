# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 02:57:01 2018

@author: YuZhang
"""

import datetime

NOW = datetime.datetime.now().strftime('%Y-%m-%d')
NOW_YEAR = datetime.datetime.now().strftime('%Y')
NOW_MONTH = datetime.datetime.now().strftime('%m')
NOW_DAY = datetime.datetime.now().strftime('%d')

#US 07
#change the orignal get_age function add age comparison function
def get_age(start, end=NOW):
    age = ""
    startlst = start.split("-")
    start_year = startlst[0]
    start_month = startlst[1]
    start_day = startlst[2]
    
    endlst = end.split("-")
    end_year = endlst[0]
    end_month = endlst[1]
    end_day = endlst[2]
    
    start_year = int(start_year)
    start_month = int(start_month)
    start_day = int(start_day)
    
    end_year = int(end_year)
    end_month = int(end_month)
    end_day = int(end_day)
  
    try:
        if datetime.datetime.strptime(end,"%Y-%m-%d") > datetime.datetime.now():
            print("Impossible date information!")
            age = "NA"
            return age
        if datetime.datetime.strptime(start,"%Y-%m-%d") > datetime.datetime.now():
            print("Impossible date information!")
            age = "NA"
            return age
    except ValueError:
        print("Impossible date information")
        age = "NA"
        return age
    
    age = end_year - start_year
    if start_month > end_month:
        age = age - 1
    elif start_month == end_month:
        if start_day > end_day:
            age = age - 1
    if age>150:
        print("Age larger than 150 is impossible!")
        age = "NA"
    return age

#US 06
def check_divorced(indi_dict,ID,month,day,div_year):
    div_year=int(div_year)
    if indi_dict[ID]["death"]!='NA':
        dod=indi_dict[ID]["death"].split('-')
        if div_year>int(dod[0]):
            print("Divorce year occur after death")
            return False
        elif div_year==int(dod[0]) and month>dod[1]:
            print("Divorce month occur after death")
            return False
        elif div_year==int(dod[0]) and month==dod[1] and day>dod[2]:
            print("Divorce day occur after death")
            return False
    else:
        return True
 
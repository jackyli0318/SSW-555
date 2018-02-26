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


def check_date(year,month,day):
    date=str(year)+"-"+str(month)+"-"+str(day)
    try:
        if datetime.datetime.strptime(date,"%Y-%m-%d") > datetime.datetime.now():
            print("Impossible date information!")
            return False
    except ValueError:
        print("Impossible date information!")
        return False
    return True


def check_married(indi_dict,ID,month,day,marry_year):
    marry_year=int(marry_year)
    dob=indi_dict[ID]["dob"].split('-')
    if dob[0]=='NA':
        print("Impossible Birthday for married!")
        return False
    else:
        marry_age = marry_year - int(dob[0])
        #print(marry_age)
        if month > int(dob[1]):
            marry_age = marry_age - 1
        elif month == int(dob[1]):
            if day > int(dob[2]):
                marry_age = marry_age - 1
        if marry_age<=14 or marry_age<0:
            print("Impossible married date!")
            return False
        else:
            return True


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

    return age
    

def check_unique(SET, ID):
    if ID in SET:
        return False, SET
    else:
        SET.add(ID)
        return True, SET




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:11:59 2018

@author: jackylee
"""
from sprint1 import check_date, check_married, get_age, check_unique, birth_before_parent_death, check_gender
from prettytable import PrettyTable
from sprint2 import set_line_num, get_line_num, marr_before_div, check_150, div_before_death, unique_name_birth, no_marriage_to_descendants
from sprint3 import birth_before_death, marr_before_death, get_married_lst, get_living_lst, get_single_lst, list_deceased, list_recent_birth
from sprint4 import siblings, nieces_nephews, Siblings_Spacing, Multiple_Births

INDI = ['INDI', 'NAME', 'SEX', 'BIRT', 'DATE', 'DEAT', 'FAMS', 'FAMC']
FAM = ['FAM', 'HUSB', 'WIFE', '_CURRENT', 'CHIL','MARR','DIV','DATE']

IGNORE_LINES = 3

ERROR_TYPE = {"I": "INDIVIDUAL", "F": "FAMILY"}

MONTH = {"JAN": "01", "FEB": "02", "MAR": "03", "APR": "04", "MAY": "05", "JUN": "06"
         , "JUL": "07", "AUG": "08", "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12"}

ERROR_LST = list()


def new_error(typ, us_num, ID, msg, error_line):
    error_msg = "ERROR: " + typ + ": US" + us_num + ": " + ID + ": " + msg + " LINE:" + str(error_line)
    return error_msg
    

def add_error(error_msg):
    ERROR_LST.append(error_msg)


def print_error(error_lst):
    if ERROR_LST:
        print("\nErrors:")
        for error in error_lst:
            print(error)
    else:
        print("All good!")


class Individual:
    def __init__(self, ID, name, gender, dob, age, alive, death, child, spouse):
        self.ID = ID  #string
        self.name = name  #string
        self.gender = gender  #string
        self.dob = dob  #string
        self.age = age  #string
        self.alive = alive  #bool
        self.death = death  #string
        self.child = child  #list
        self.spouse = spouse  #list


class Family:
    def __init__(self, ID, married, divorced, husb_id, husb_name, wife_id, wife_name, children):
        self.ID = ID  #string
        self.married =  married  #string
        self.divorced = divorced  #string "Yes" / "NA"
        self.husb_id = husb_id  #string
        self.husb_name = husb_name  #string
        self.wife_id = wife_id  #string
        self.wife_name = wife_name  #string
        self.children = children  #list

def new_indi():
    indi = {
            "ID": "",  "name": "",  "gender": "",  "dob": "",  "age": "",  "alive": True,
            "death": "",  "child": "NA", "spouse": "NA", 'line_dict':{}
            }
    return indi


def create_indi(tmp_indi):
    new_indi = Individual(tmp_indi["ID"], tmp_indi["name"], tmp_indi["gender"], 
                          tmp_indi["dob"], tmp_indi["age"], tmp_indi["alive"], tmp_indi["death"], tmp_indi["child"], tmp_indi["spouse"])
    return new_indi


def new_fam():
    fam = {
            "ID": "",  "married": "",  "divorced": "",  "husb_id": "",  "husb_name": "",  "wife_id": "",
             "wife_name": "",  "children": {}, 'line_dict':{}
            }
    return fam


def create_fam(tmp_fam):
    new_fam = Family(tmp_fam["ID"], tmp_fam["married"], tmp_fam["divorced"], 
                          tmp_fam["husb_id"], tmp_fam["husb_name"], tmp_fam["wife_id"], tmp_fam["wife_name"], tmp_fam["children"])
    return new_fam


def read_indi(indi_lst):
    indi_dict = dict()
    
    INDI_SET = set()
    begin_num = 0
 
    for indi in indi_lst:
        tmp_indi = new_indi()
        
        linelst = indi.strip().split("|")
        line_num = 0
        
        for line in linelst:
            line_num += 1
            wordlst = line.strip().split(" ")
            
            # line number field
            field = ""
            
            # get the line number
            if "LINE" in wordlst:
                begin_num = int(wordlst[2])
                line_num += begin_num-2
                continue
            
            if "INDI" in wordlst:
                tmp = wordlst[2]
                wordlst[2] = wordlst[1]
                wordlst[1] = tmp
            
            if wordlst[1] == "BIRT":
                datetag = "BIRT"
                continue
            elif wordlst[1] == "DEAT":
                datetag = "DEAT"
                tmp_indi['alive'] = False
                continue
            elif wordlst[1] != "DATE":
                datetag = ""
            
            extra_field = ""
            if datetag == "BIRT" or datetag == "DEAT":
                extra_field = datetag + "_"
            
            field =  extra_field + wordlst[1]
            tmp_indi = set_line_num(tmp_indi, field, line_num)
            
            # if id is not unique, we will add ** at the end of the ID for checking
            if wordlst[1] == "INDI":
                tmpID = wordlst[2].split("@")[1]
                tmpbool, INDI_SET = check_unique(INDI_SET, wordlst[2])
                if tmpbool:
                    tmp_indi['ID'] = tmpID
                else:
                    tmp_indi['ID'] = tmpID + "**"
                    error_msg = tmpID+": not unique!"
                    error_line = get_line_num(tmp_indi, field)
                    error_msg = new_error(ERROR_TYPE['I'], "22", tmp_indi['ID'], error_msg, error_line)
                    add_error(error_msg)
                continue
            
            if wordlst[1] == "NAME":
                argu = ""
                for i in range(2,len(wordlst)):
                    argu += wordlst[i] + " "
                tmp_indi['name'] = argu
                
                # file line + 3 to ignore the given name lines
                line_num += IGNORE_LINES
                continue
            
            if wordlst[1] == "SEX":
                tmp_indi['gender'] = wordlst[2]
                continue
            
                
            if datetag == "BIRT":
                day = wordlst[2]
                if len(day) < 2:
                    day = "0" + day
                month = MONTH.get(wordlst[3], "")
                birtyear = wordlst[4]
                birthday = birtyear + "-" + month + "-" + day
                
                if check_date(birthday)=="01":
                    tmp_indi['dob'] = "NA"
                    
                    error_msg = "Birthday " + birthday + " is impossible!"
                    error_line = get_line_num(tmp_indi, field)
                    
                    error_msg = new_error(ERROR_TYPE['I'], "01", tmp_indi['ID'], error_msg, error_line)
                    add_error(error_msg)
                elif check_date(birthday)=="42":
                    tmp_indi['dob'] = "NA"
                    error_msg = "Birthday " + birthday + " is impossible!"
                    error_line = get_line_num(tmp_indi, field)
                    error_msg = new_error(ERROR_TYPE['I'], "42", tmp_indi['ID'], error_msg, error_line)
                    add_error(error_msg)
                    
                else:
                    tmp_indi['dob'] = birtyear + "-" + month + "-" + day
                    
                age = get_age(tmp_indi['dob']) 
                if age == "NA":
                    error_msg = "Age of " + tmp_indi['ID'] + " " + birthday + " is impossible!"
                    error_line = get_line_num(tmp_indi, field)
                    error_msg = new_error(ERROR_TYPE['I'], "27", tmp_indi['ID'], error_msg, error_line)
                    add_error(error_msg)
                
                tmp_indi['age'] = age
                datetag = ""
                
            elif datetag == "DEAT":
                day = wordlst[2]
                if len(day) < 2:
                    day = "0" + day
                month = MONTH.get(wordlst[3], "")
                deatyear = wordlst[4]
                deathdate = deatyear + "-" + month + "-" + day
                
                if check_date(deathdate)=="01":
                    tmp_indi['death'] = "NA"
                    error_msg = "Death " + deathdate + " is impossible!"
                    error_line = get_line_num(tmp_indi, field)
                    error_msg = new_error(ERROR_TYPE['I'], "01", tmp_indi['ID'], error_msg, error_line)
                    add_error(error_msg)
                elif check_date(deathdate)=="42":
                    tmp_indi['death'] = "NA"
                    error_msg = "Death " + deathdate + " is impossible!"
                    error_line = get_line_num(tmp_indi, field)
                    error_msg = new_error(ERROR_TYPE['I'], "42", tmp_indi['ID'], error_msg, error_line)
                    add_error(error_msg)
                else:
                    tmp_indi['death'] = deathdate
                
                age = get_age(tmp_indi['dob'], tmp_indi['death'])
                if age == "NA":
                    error_msg = "Age of " + tmp_indi['ID'] + " is impossible!"
                    error_line = get_line_num(tmp_indi, field)
                    error_msg = new_error(ERROR_TYPE['I'], "27", tmp_indi['ID'], error_msg, error_line)
                    add_error(error_msg)
                tmp_indi['age'] = age
                datetag = ""
            

        if tmp_indi.get("death") == "":
            tmp_indi["death"] = "NA"
        
        uq_flag, INDI_SET =  unique_name_birth(INDI_SET, tmp_indi)
        if not uq_flag:
            field = 'NAME'
            error_msg = "Name and birth of " + tmp_indi['ID'] + " is not unique!"
            error_line = get_line_num(tmp_indi, field)
            error_msg = new_error(ERROR_TYPE['I'], "23", tmp_indi['ID'], error_msg, error_line)
            add_error(error_msg)
            
        indi_dict[tmp_indi["ID"]] = tmp_indi
        
        
    return indi_dict

                                        
            
def read_fam(fam_lst, indi_dict):
    fam_dict = dict()
    FAM_SET = set()
    
    begin_num = 0
    
    for fam in fam_lst:
        line_num = 0
        
        tmp_fam = new_fam()
        
        linelst = fam.strip().split("|")
        for line in linelst:
            line_num += 1
            wordlst = line.strip().split(" ")
            
            # line number field
            field = ""
            
            # get the line number
            if "LINE" in wordlst:
                begin_num = int(wordlst[2])
                line_num += begin_num-2
#                print(begin_num)
                continue
            
            if "FAM" in wordlst:
                tmp = wordlst[2]
                wordlst[2] = wordlst[1]
                wordlst[1] = tmp
            
            if wordlst[1] == "MARR":
                datetag = "MARR"
                continue
            elif wordlst[1] == "DIV":
                datetag = "DIV"
                continue
            elif wordlst[1] != "DATE":
                datetag = ""
            
            extra_field = ""
            if datetag == "MARR" or datetag == "DIV":
                extra_field = datetag + "_"
            
            field =  extra_field + wordlst[1]
            tmp_fam = set_line_num(tmp_fam, field, line_num)
            
            # if id is not unique, we will add ** at the end of the ID for checking
            if wordlst[1] == "FAM":
                field = 'FAM'
                tmpID = wordlst[2].split("@")[1]
                tmpbool, FAM_SET = check_unique(FAM_SET, wordlst[2])
                if tmpbool:
                    tmp_fam['ID'] = tmpID
                else:
                    tmp_fam['ID'] = tmpID + "**"
                    error_msg = tmpID+": not unique!"
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "22", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)
                continue
            
            if wordlst[1] == "HUSB":
                husb_id = wordlst[2].split("@")[1]
                tmp_fam['husb_id'] = husb_id
                tmp_fam['husb_name'] = indi_dict[husb_id]["name"]
            
            if wordlst[1] == "WIFE":
                wife_id = wordlst[2].split("@")[1]
                tmp_fam['wife_id'] = wife_id
                tmp_fam['wife_name'] = indi_dict[wife_id]["name"]
                
            if wordlst[1] == "CHIL":
                child_id = wordlst[2].split("@")[1].strip()
#                print(child_id)
                if tmp_fam.get("children"):
                    
                    tmp_fam["children"].add(child_id)
                else:
                    tmp_fam["children"] = {child_id}
                    
            
                
            if datetag == "MARR":
                day = wordlst[2]
                if len(day) < 2:
                    day = "0" + day
                month = MONTH.get(wordlst[3], "")
                marryear = wordlst[4]
                marrdate = marryear + "-" + month + "-" + day 
                
                h_birth = indi_dict[tmp_fam['husb_id']].get('dob', "NA")
                w_birth = indi_dict[tmp_fam['wife_id']].get('dob', "NA")
                
                # US01 US42
                if check_date(marrdate)=="01":
                    tmp_fam['married'] = "NA"
                    error_msg = "Marriage " + marrdate + " is impossible!"
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "01", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)
                elif check_date(marrdate)=="42":
                    tmp_fam['married'] = "NA"
                    error_msg = "Marriage " + marrdate + " is impossible!"
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "42", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)
                # US02 US10
                elif check_married(h_birth, marrdate)=="02" or check_married(w_birth, marrdate)=="02":
                    tmp_fam['married'] = "NA"
                    error_msg = "Marriage " + marrdate + " should occur after the birth of both husband and wife!"
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "02", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)
                elif check_married(h_birth, marrdate)=="10" or check_married(w_birth, marrdate)=="10":
                    tmp_fam['married'] = "NA"
                    error_msg = "Marriage " + marrdate + " should occur after the husband or wife is 14 years old!"
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "10", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)
                else:
                    tmp_fam['married'] = marryear + "-" + month + "-" + day 
                
                #US 05
                flag, who = marr_before_death(indi_dict, marrdate, tmp_fam['husb_id'], tmp_fam['wife_id'])
                if not flag:
                    error_msg = "Marriage " + marrdate + " should occur before the death of "
                    if who == "hs":
                        error_who = tmp_fam['husb_name']
                    elif who == "wf":
                        error_who = tmp_fam['wife_name'] 
                    else:
                        error_who = tmp_fam['husb_name'] +" and " + tmp_fam['wife_name']
                    error_msg = error_msg + error_who
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "05", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)
               
            
            elif datetag == "DIV":
                day = wordlst[2]
                if len(day) < 2:
                    day = "0" + day
                month = MONTH.get(wordlst[3], "")
                divyear = wordlst[4]
                divdate = divyear + "-" + month + "-" + day 
                
                # US01 US42
                if check_date(divdate)=="01":
                    tmp_fam['divorced'] = "NA"
                    error_msg = "Divorce " + divdate + " is impossible!"
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "01", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)
                elif check_date(divdate)=="42":
                    tmp_fam['divorced'] = "NA"
                    error_msg = "Divorce " + divdate + " is impossible!"
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "42", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)
                else:
                    tmp_fam['divorced'] = divdate
                
                # US06
                flag, who = div_before_death(indi_dict, divdate, tmp_fam['husb_id'], tmp_fam['wife_id'])
                if not flag:
                    error_msg = "Divorce " + divdate + " should occur before the death of "
                    if who == "hs":
                        error_who = tmp_fam['husb_name']
                    elif who == "wf":
                        error_who = tmp_fam['wife_name'] 
                    else:
                        error_who = tmp_fam['husb_name'] +" and " + tmp_fam['wife_name']
                    error_msg = error_msg + error_who
                    error_line = get_line_num(tmp_fam, field)
                    error_msg = new_error(ERROR_TYPE['F'], "06", tmp_fam['ID'], error_msg, error_line)
                    add_error(error_msg)                    
                    
            if tmp_fam.get("divorced") == "":
                    tmp_fam['divorced'] = "NA"

        fam_dict[tmp_fam["ID"]] = tmp_fam
        
        
    return fam_dict


def re_read_fam(indi_dict, fam_dict):
#    spouse
    marr_living = list()
    single_living = list()
    info_dict = dict()
    
    for key in fam_dict:
        tmp_fam = fam_dict[key]
        husb_id = tmp_fam['husb_id']
        wife_id = tmp_fam['wife_id']
        children = tmp_fam["children"]
        indi_dict[husb_id]['spouse'] = "{'"+key+"'}"
        indi_dict[wife_id]['spouse'] = "{'"+key+"'}"
        
        hdeath = indi_dict[husb_id]["death"]
        wdeath = indi_dict[wife_id]["death"]
        
        for chld in children:
            indi_dict[chld]['child'] = "{'"+key+"'}"
            
            cbirth = indi_dict[chld]['dob']
            
            # US09
            if not birth_before_parent_death(cbirth,hdeath,wdeath):
                tmp_indi = indi_dict[chld]
                field = "BIRT_DATE"
                error_msg = "The birth of " + chld + " should occur before the death of his/her parents!"
                error_line = get_line_num(tmp_indi, field)
                error_msg = new_error(ERROR_TYPE['F'], "09", key, error_msg, error_line)
                add_error(error_msg)
                
        flag, tmp_id = check_gender(key, fam_dict, indi_dict)
        
        # US21
        if not flag:
            field = 'SEX'
            tmp_indi = indi_dict[tmp_id]
            error_msg = "Current gender for the role: " + tmp_indi.get('name', "")  + " of family " + key + " is wrong!"
            error_line = get_line_num(tmp_indi, field)
            error_msg = new_error(ERROR_TYPE['F'], "21", key, error_msg, error_line)
            add_error(error_msg)
        
        # US04
        if not marr_before_div(tmp_fam):
            field = 'DIV_DATE'
            error_msg = "Family: "+ key + " The marrage should occur before the divorce!"
            error_line = get_line_num(tmp_fam, field)
            error_msg = new_error(ERROR_TYPE['F'], "04", key, error_msg, error_line)
            add_error(error_msg)
        
        # US17
        if not no_marriage_to_descendants(tmp_fam, fam_dict):
            field = 'CHIL'
            error_msg = "Family: "+ key + " The marrage should not occur with descendants!"
            error_line = get_line_num(tmp_fam, field)
            error_msg = new_error(ERROR_TYPE['F'], "17", key, error_msg, error_line)
            add_error(error_msg)
        
        # US18
        husb_flag, husb_fam = siblings(tmp_fam['husb_id'], tmp_fam, fam_dict)
        wife_flag, wife_fam = siblings(tmp_fam['wife_id'], tmp_fam, fam_dict)
        if not husb_flag:
            field = 'CHIL'
            error_msg = "Family: "+ key + ": the couple are siblings. They should not marry with each other!"
            error_line = get_line_num(husb_fam, field)
            error_msg = new_error(ERROR_TYPE['F'], "18", key, error_msg, error_line)
            add_error(error_msg)
        if not wife_flag:
            field = 'CHIL'
            error_msg = "Family: "+ key + ": the couple are siblings. They should not marry with each other!"
            error_line = get_line_num(wife_fam, field)
            error_msg = new_error(ERROR_TYPE['F'], "18", key, error_msg, error_line)
            add_error(error_msg)
        
        # US20
        aunt_flag = nieces_nephews(tmp_fam['husb_id'], tmp_fam['wife_id'], fam_dict)
        uncle_flag = nieces_nephews(tmp_fam['wife_id'], tmp_fam['husb_id'], fam_dict)
        if not aunt_flag or not uncle_flag:
            if not uncle_flag:
                field = 'HUSB'
            else:
                field = 'WIFE'
            error_msg = "Family: "+ key + " The marriage should not occur with nieces or nepthews!"
            error_line = get_line_num(tmp_fam, field)
            error_msg = new_error(ERROR_TYPE['F'], "20", key, error_msg, error_line)
            add_error(error_msg)
        
        # US13
        if not Siblings_Spacing(tmp_fam, indi_dict):
            field = 'CHIL'
            error_msg = "Family: "+ key + " Birth dates of siblings in this family should be more than 8 months apart or less than 2 days apart!"
            error_line = get_line_num(tmp_fam, field)
            error_msg = new_error(ERROR_TYPE['F'], "13", key, error_msg, error_line)
            add_error(error_msg)
            
        # US14
        if not Multiple_Births(tmp_fam, indi_dict):
            field = 'CHIL'
            error_msg = "Family: "+ key + " Multiple births is impossible. No more than five siblings in this family should be born at the same time!"
            error_line = get_line_num(tmp_fam, field)
            error_msg = new_error(ERROR_TYPE['F'], "14", key, error_msg, error_line)
            add_error(error_msg)
        
        marr_living = get_married_lst(tmp_fam, marr_living)
        marr_living = get_living_lst(marr_living, indi_dict)
        
        single_living = get_single_lst(indi_dict, marr_living)
        
        
    
    marr_living.sort()
    single_living.sort()
    info_dict['marr_alive'] =  marr_living
    info_dict['single_alive'] = single_living
    
    return indi_dict, fam_dict, info_dict



def re_read_indi(indi_dict, info_dict):
    recent_birth_lst = list()
    deceased_lst = list()
    
    for key in indi_dict:
        tmp_indi = indi_dict[key]
        age = tmp_indi['age']
        # US07
        if age != 'NA':
            if check_150(age) == "NA":
                field = "BIRT_DATE"
                error_msg = "Age of " + tmp_indi['ID'] + "" + " is impossible to be greater than 150!"
                error_line = get_line_num(tmp_indi, field)
                error_msg = new_error(ERROR_TYPE['I'], "07", tmp_indi['ID'], error_msg, error_line)
                add_error(error_msg)
                indi_dict[key]['age'] = "NA"
                
        # US03 
        dob=tmp_indi['dob']
        death=tmp_indi['death']
        if not birth_before_death(dob,death):
            field = "BIRT_DATE"
            error_msg = "The birth of " + tmp_indi['ID'] + "" + " happens after death date!"
            error_line = get_line_num(tmp_indi, field)
            error_msg = new_error(ERROR_TYPE['I'], "03", tmp_indi['ID'], error_msg, error_line)
            add_error(error_msg)
            indi_dict[key]['age'] = "NA"
                
        # US 29
        deceased_lst = list_deceased(tmp_indi, deceased_lst)
        info_dict['deceased_lst'] = sorted(deceased_lst)
        
        # US 37
        recent_birth_lst = list_recent_birth(tmp_indi, recent_birth_lst)
        info_dict['recent_birth_lst'] = sorted(recent_birth_lst)
        
        
    return indi_dict, info_dict


def run(filename):
    line_num = 0
    begin_line = "0"
    try:
        f = open(filename, 'r', encoding='utf-8')
#        output_file = open("outputs.txt", 'w+', encoding='utf-8')
    except FileNotFoundError:
        return "File not found!"
    else:
        readtag = "NA"
        
        indi_lst = list()
        fam_lst = list()
        
        tmp_line = ""
        
        lines = f.readlines()
        for line in lines:
            line_num += 1
            
            wordlst = line.strip().split(" ")
            if len(wordlst) < 2:
#                print("next line")
                continue
            
            # adjust the postion of "FAM" and "INDI"
            if "FAM" in wordlst or "INDI" in wordlst:
                tmp = wordlst[2]
                wordlst[2] = wordlst[1]
                wordlst[1] = tmp
                
            # if found the next one, append the former one
            if "FAM" == wordlst[1] or "INDI" == wordlst[1]:
                if readtag == "FAM":
                    if tmp_line != "":
                        tmp_line = begin_line + tmp_line
                        fam_lst.append(tmp_line)
                        
                else:
                    if tmp_line != "":
                        tmp_line = begin_line + tmp_line
                        indi_lst.append(tmp_line)

            if "INDI" == wordlst[1]:
                begin_line = "0 LINE "+str(line_num) + "|"
                readtag = "INDI"
                tmp_line = line.strip()
                continue
                
            if "FAM" == wordlst[1]:
                begin_line = "0 LINE "+str(line_num) + "|"
                readtag = "FAM"
                tmp_line = line.strip()
                continue
            
            if readtag == "INDI":
                if wordlst[1] in INDI:
                    tmp_line = tmp_line + "|" + line.strip() 
            
            if readtag == "FAM":
                if wordlst[1] in FAM:
                    tmp_line = tmp_line + "|" + line.strip()
            
            # final line and append the rest part
            if "TRLR" == wordlst[1]:
                if readtag == "FAM":
                    if tmp_line != "":
                        tmp_line = begin_line + tmp_line
                        fam_lst.append(tmp_line)
                else:
                    if tmp_line != "":
                        tmp_line = begin_line + tmp_line
                        indi_lst.append(tmp_line)
                tmp_line = ""
        
        # if the last one not gets added in the list, append it.
        if "FAM" in tmp_line:
            tmp_line = begin_line + tmp_line
            fam_lst.append(tmp_line)
        if "INDI" in tmp_line:
            tmp_line = begin_line + tmp_line
            indi_lst.append(tmp_line)
            
#        print(indi_lst)
        
        indi_dict = read_indi(indi_lst)
        fam_dict = read_fam(fam_lst, indi_dict)
        indi_dict, fam_dict, info_dict = re_read_fam(indi_dict, fam_dict)
        indi_dict, info_dict = re_read_indi(indi_dict, info_dict)
#        print(indi_dict)
#        print("")
#        print(fam_dict)
#        print("")
        
        f.close()
        return indi_dict, fam_dict, info_dict
            
            
        
if __name__ == "__main__":
    
#    indi_dict, fam_dict, info_dict = run('Family.ged')
    indi_dict, fam_dict, info_dict = run('bugFamily.ged')
    
    print("Individuals")
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    for key in indi_dict:
        indi = indi_dict[key]
        x.add_row([indi["ID"], indi["name"], indi["gender"], indi["dob"], indi["age"], indi["alive"]
        , indi["death"], indi["child"], ""+indi["spouse"]+""])
    print (x)
    
    print("")
    print("Families")
    x = PrettyTable()
    x.field_names = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 
                     'Wife ID', 'Wife Name', 'Children']
    for key in fam_dict:
        fam = fam_dict[key]
        x.add_row([fam["ID"], fam["married"], fam["divorced"], fam["husb_id"], fam["husb_name"], 
                  fam["wife_id"], fam["wife_name"], fam["children"]])
    print (x)
    
    print("Living married: ")
    print(info_dict['marr_alive'])
    
    print("Living single: ")
    print(info_dict['single_alive'])
    
    print("Deceased list: ")
    print(info_dict['deceased_lst'])
    
    print("Recent birth list: ")
    print(info_dict['recent_birth_lst'])
    
#    print_error(sorted(ERROR_LST))
    print_error(ERROR_LST)
    
    
    
#    print("")
#    for key in indi_dict:
#        indi = indi_dict[key]
#        print(indi.get('line_dict'))
#        print("")
#        
#    print("")
#    for key in fam_dict:
#        fam = fam_dict[key]
#        print(fam.get('line_dict'))
#        print("")
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
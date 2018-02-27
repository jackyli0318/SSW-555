#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:11:59 2018

@author: jackylee
"""
from sprint1 import check_date, check_married, get_age, check_unique, birth_before_parent_death, check_gender
from prettytable import PrettyTable

INDI = ['INDI', 'NAME', 'SEX', 'BIRT', 'DATE', 'DEAT', 'FAMS', 'FAMC']
FAM = ['FAM', 'HUSB', 'WIFE', '_CURRENT', 'CHIL','MARR','DIV','DATE']

ERROR_TYPE = {"I": "INDIVIDUAL", "F": "FAMILY"}

MONTH = {"JAN": "01", "FEB": "02", "MAR": "03", "APR": "04", "MAY": "05", "JUN": "06"
         , "JUL": "07", "AUG": "08", "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12"}

ERROR_LST = list()


def new_error(typ, us_num, ID, msg):
    error_msg = "ERROR: " + typ + ": US" + us_num + ": " + ID + ": " + msg 
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
            "death": "",  "child": "NA", "spouse": "NA"
            }
    return indi


def create_indi(tmp_indi):
    new_indi = Individual(tmp_indi["ID"], tmp_indi["name"], tmp_indi["gender"], 
                          tmp_indi["dob"], tmp_indi["age"], tmp_indi["alive"], tmp_indi["death"], tmp_indi["child"], tmp_indi["spouse"])
    return new_indi


def new_fam():
    fam = {
            "ID": "",  "married": "",  "divorced": "",  "husb_id": "",  "husb_name": "",  "wife_id": "",
             "wife_name": "",  "children": {}
            }
    return fam


def create_fam(tmp_fam):
    new_fam = Family(tmp_fam["ID"], tmp_fam["married"], tmp_fam["divorced"], 
                          tmp_fam["husb_id"], tmp_fam["husb_name"], tmp_fam["wife_id"], tmp_fam["wife_name"], tmp_fam["children"])
    return new_fam


def read_indi(indi_lst):
    indi_dict = dict()
    
    INDI_SET = set()
 
    for indi in indi_lst:
        tmp_indi = new_indi()
        
        linelst = indi.strip().split("|")
        for line in linelst:
            wordlst = line.strip().split(" ")
            
            if "INDI" in wordlst:
                tmp = wordlst[2]
                wordlst[2] = wordlst[1]
                wordlst[1] = tmp
            
            # if id is not unique, we will add ** at the end of the ID for checking
            if wordlst[1] == "INDI":
                tmpID = wordlst[2].split("@")[1]
                tmpbool, INDI_SET = check_unique(INDI_SET, wordlst[2])
                if tmpbool:
                    tmp_indi['ID'] = tmpID
                else:
                    tmp_indi['ID'] = tmpID + "**"
                    error_msg = tmpID+": not unique!"
                    error_msg = new_error(ERROR_TYPE['I'], "22", tmp_indi['ID'], error_msg)
                    add_error(error_msg)
                continue
            
            if wordlst[1] == "NAME":
                argu = ""
                for i in range(2,len(wordlst)):
                    argu += wordlst[i] + " "
                tmp_indi['name'] = argu
                continue
            
            if wordlst[1] == "SEX":
                tmp_indi['gender'] = wordlst[2]
                continue
            
            if wordlst[1] == "BIRT":
                datetag = "BIRT"
                continue
            elif wordlst[1] == "DEAT":
                datetag = "DEAT"
                tmp_indi['alive'] = False
                continue
            elif wordlst[1] != "DATE":
                datetag = ""
                
            if datetag == "BIRT":
                day = wordlst[2]
                if len(day) < 2:
                    day = "0" + day
                month = MONTH.get(wordlst[3], "")
                birtyear = wordlst[4]
                birthday = birtyear + "-" + month + "-" + day
                
                if check_date(birthday)==False:
                    tmp_indi['dob'] = "NA"
                    error_msg = "Birthday " + birthday + " is impossible!"
                    error_msg = new_error(ERROR_TYPE['I'], "01", tmp_indi['ID'], error_msg)
                    add_error(error_msg)
                else:
                    tmp_indi['dob'] = birtyear + "-" + month + "-" + day
                    
                age = get_age(tmp_indi['dob']) 
                if age == "NA":
                    error_msg = "Age of " + tmp_indi['ID'] + " " + birthday + " is impossible!"
                    error_msg = new_error(ERROR_TYPE['I'], "27", tmp_indi['ID'], error_msg)
                    add_error(error_msg)
                tmp_indi['age'] = age
                
            elif datetag == "DEAT":
                day = wordlst[2]
                if len(day) < 2:
                    day = "0" + day
                month = MONTH.get(wordlst[3], "")
                deatyear = wordlst[4]
                deathdate = deatyear + "-" + month + "-" + day
                
                if check_date(deathdate)==False:
                    tmp_indi['death'] = "NA"
                    error_msg = "Death " + deathdate + " is impossible!"
                    error_msg = new_error(ERROR_TYPE['I'], "01", tmp_indi['ID'], error_msg)
                    add_error(error_msg)
                else:
                    tmp_indi['death'] = deathdate
                
                age = get_age(tmp_indi['dob'], tmp_indi['death'])
                if age == "NA":
                    error_msg = "Age of " + tmp_indi['ID'] + " is impossible!"
                    error_msg = new_error(ERROR_TYPE['I'], "27", tmp_indi['ID'], error_msg)
                    add_error(error_msg)
                tmp_indi['age'] = age

        if tmp_indi.get("death") == "":
            tmp_indi["death"] = "NA"
            
        indi_dict[tmp_indi["ID"]] = tmp_indi
        
    return indi_dict

                                        
            
def read_fam(fam_lst, indi_dict):
    fam_dict = dict()
    FAM_SET = set()
    
    for fam in fam_lst:
        tmp_fam = new_fam()
        
        linelst = fam.strip().split("|")
        for line in linelst:
            wordlst = line.strip().split(" ")
            
            if "FAM" in wordlst:
                tmp = wordlst[2]
                wordlst[2] = wordlst[1]
                wordlst[1] = tmp
            
            # if id is not unique, we will add ** at the end of the ID for checking
            if wordlst[1] == "FAM":
                tmpID = wordlst[2].split("@")[1]
                tmpbool, FAM_SET = check_unique(FAM_SET, wordlst[2])
                if tmpbool:
                    tmp_fam['ID'] = tmpID
                else:
                    tmp_fam['ID'] = tmpID + "**"
                    error_msg = tmpID+": not unique!"
                    error_msg = new_error(ERROR_TYPE['F'], "22", tmp_fam['ID'], error_msg)
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
                    
            if wordlst[1] == "MARR":
                datetag = "MARR"
                continue
            elif wordlst[1] == "DIV":
                datetag = "DIV"
                continue
            elif wordlst[1] != "DATE":
                datetag = ""
                
            if datetag == "MARR":
                day = wordlst[2]
                if len(day) < 2:
                    day = "0" + day
                month = MONTH.get(wordlst[3], "")
                marryear = wordlst[4]
                marrdate = marryear + "-" + month + "-" + day 
                
                h_birth = indi_dict[tmp_fam['husb_id']].get('dob', "NA")
                w_birth = indi_dict[tmp_fam['wife_id']].get('dob', "NA")
                
                if check_date(marrdate)==False:
                    tmp_fam['married'] = "NA"
                    error_msg = "Marriage " + marrdate + " is impossible!"
                    error_msg = new_error(ERROR_TYPE['F'], "01", tmp_fam['ID'], error_msg)
                    add_error(error_msg)

                elif check_married(h_birth, marrdate)==False or check_married(w_birth, marrdate)==False:
                    tmp_fam['married'] = "NA"
                    error_msg = "Marriage " + marrdate + " should occur after the birth of both husband and wife!"
                    error_msg = new_error(ERROR_TYPE['F'], "02", tmp_fam['ID'], error_msg)
                    add_error(error_msg)
                else:
                    tmp_fam['married'] = marryear + "-" + month + "-" + day 
               
            
            elif datetag == "DIV":
                day = wordlst[2]
                if len(day) < 2:
                    day = "0" + day
                month = MONTH.get(wordlst[3], "")
                divyear = wordlst[4]
                divdate = divyear + "-" + month + "-" + day 
                
                if check_date(divdate)==False:
                    tmp_fam['divorced'] = "NA"
                    error_msg = "Divorce " + divdate + " is impossible!"
                    error_msg = new_error(ERROR_TYPE['F'], "01", tmp_fam['ID'], error_msg)
                    add_error(error_msg)
                else:
                    tmp_fam['divorced'] = divdate
           
            if tmp_fam.get("divorced") == "":
                    tmp_fam['divorced'] = "NA"

        fam_dict[tmp_fam["ID"]] = tmp_fam
        
        
    return fam_dict


def re_read_dicts(indi_dict, fam_dict):
#    spouse
    for key in fam_dict:
        
        husb_id = fam_dict[key]['husb_id']
        wife_id = fam_dict[key]['wife_id']
        children = fam_dict[key]["children"]
        indi_dict[husb_id]['spouse'] = "{'"+key+"'}"
        indi_dict[wife_id]['spouse'] = "{'"+key+"'}"
        
        hdeath = indi_dict[husb_id]["death"]
        wdeath = indi_dict[wife_id]["death"]
        
        for chld in children:
            indi_dict[chld]['child'] = "{'"+key+"'}"
            
            cbirth = indi_dict[chld]['dob']
            
            if not birth_before_parent_death(cbirth,hdeath,wdeath):
                error_msg = "The birth of " + chld + " should occur before the death of his/her parents!"
                error_msg = new_error(ERROR_TYPE['F'], "09", key, error_msg)
                add_error(error_msg)
                
        if not check_gender(key, fam_dict, indi_dict):
            error_msg = "Current gender for the role of family " + key + " is wrong!"
            error_msg = new_error(ERROR_TYPE['F'], "21", key, error_msg)
            add_error(error_msg)
        
        
    return indi_dict, fam_dict


def run(filename):
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
            wordlst = line.strip().split(" ")
            if len(wordlst) < 2:
                print("next line")
                continue
            if "FAM" in wordlst or "INDI" in wordlst:
                tmp = wordlst[2]
                wordlst[2] = wordlst[1]
                wordlst[1] = tmp
                

            if "FAM" == wordlst[1] or "INDI" == wordlst[1]:
                if readtag == "FAM":
                    if tmp_line != "":
                        fam_lst.append(tmp_line)
                else:
                    if tmp_line != "":
                        indi_lst.append(tmp_line)

            if "INDI" == wordlst[1]:
                readtag = "INDI"
                tmp_line = line.strip()
                continue
                
            if "FAM" == wordlst[1]:
                readtag = "FAM"
                tmp_line = line.strip()
                continue
            
            if readtag == "INDI":
                if wordlst[1] in INDI:
                    tmp_line = tmp_line + "|" + line.strip() 
            
            if readtag == "FAM":
                if wordlst[1] in FAM:
                    tmp_line = tmp_line + "|" + line.strip()
            
            if "TRLR" == wordlst[1]:
                if readtag == "FAM":
                    if tmp_line != "":
                        fam_lst.append(tmp_line)
                else:
                    if tmp_line != "":
                        indi_lst.append(tmp_line)
                tmp_line = ""
                
        if "FAM" in tmp_line:
            fam_lst.append(tmp_line)
        if "INDI" in tmp_line:
            indi_lst.append(tmp_line)
        
        indi_dict = read_indi(indi_lst)
        fam_dict = read_fam(fam_lst, indi_dict)
        indi_dict, fam_dict = re_read_dicts(indi_dict, fam_dict)
        
#        print(indi_dict)
#        print("")
#        print(fam_dict)
#        print("")
        
        f.close()
        return indi_dict, fam_dict
            
            
        
if __name__ == "__main__":
    
#    indi_dict, fam_dict = run('Family.ged')
    indi_dict, fam_dict = run('bugFamily.ged')
    
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
    
    print_error(ERROR_LST)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
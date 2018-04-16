#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import datetime


# US10 & US42 are in sprint1.py


# US18 & US20
def get_siblings_fam(indi_id, fam_dict):
    for key in fam_dict:
        fam = fam_dict[key]
        if indi_id in fam['children']:
            return fam


# US18
#def get_couple_lst(fam_dict):
#    couple_lst = list()
#    for key in fam_dict:
#        fam = fam_dict[key]
#        couple = list()
#        couple.append(fam['husb_id'])
#        couple.append(fam['wife_id'])
#        couple_lst.append(couple)
#    return couple_lst



def siblings(indi_id, tmp_fam, fam_dict):
    fam = get_siblings_fam(indi_id, fam_dict)
    sibling_set = None
    if fam:
        sibling_set = fam['children']
        couple_set = {tmp_fam['husb_id'], tmp_fam['wife_id']} 
    if sibling_set:
        if len(sibling_set - couple_set) == len(sibling_set)-2:
                return False, fam
    return True, None



# US20
def nieces_nephews(indi_id, spouse_id, fam_dict):
    # [ [], [], []]          list(  list()   )
    nieces_nephews_lst = list()
    fam = get_siblings_fam(indi_id, fam_dict)
    sibling_set = None
    if fam:
        sibling_set = fam['children']
    if sibling_set:
        sibling_set = sibling_set - set(indi_id)

        for key in fam_dict:
            fam = fam_dict[key]
            if fam['husb_id'] in sibling_set or fam['wife_id'] in sibling_set:
                nieces_nephews_lst += list(fam['children'])
        if spouse_id in nieces_nephews_lst:
            return False
    return True


    

# US 13
def Siblings_Spacing(tmp_fam, indi_dict):
    children = list(tmp_fam['children'])
    for i in range(len(children)):
        child_i = indi_dict[children[i]]
        try:
            dobi = datetime.datetime.strptime(child_i['dob'],"%Y-%m-%d")
        except ValueError:
            continue
        for j in range(i + 1, len(children)):
            child_j = indi_dict[children[j]]
            try:
                dobj = datetime.datetime.strptime(child_j['dob'],"%Y-%m-%d")
            except ValueError:
                continue
            if 2 <= abs((dobi - dobj).days) <= 30.4 * 8:
                return False
    return True


# US 14
def Multiple_Births(tmp_fam, indi_dict):
    children = tmp_fam['children']
    d = dict()
    for child in children:
        dob = indi_dict[child]['dob']
        if dob == 'NA':
            continue
        if dob in d:
            d[dob] += 1
        else:
            d[dob] = 1
    for key in d:
        if d[key] > 5:
            return False
    return True



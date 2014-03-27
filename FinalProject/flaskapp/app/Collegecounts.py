#!/usr/local/bin python
# -*- coding: utf8 -*-
from glob import iglob
import os.path
import json,pymongo
import codecs
import json
import csv
import sys
import numpy as np
from pymongo import MongoClient

database = 'postsecondary'
connection = pymongo.MongoClient(host="ec2-54-226-101-255.compute-1.amazonaws.com", port=27017)
db = getattr(connection,database)
coll=db['production']
#sys.exit(0)

def getByDot(obj, ref, strict=True):
    """
    Use MongoDB style 'something.by.dot' syntax to retrieve objects from Python dicts.
    
    This also accepts nested arrays, and accommodates the '.XX' syntax that variety.js
    produces.
    
    Usage:
       >>> x = {"top": {"middle" : {"nested": "value"}}}
       >>> q = 'top.middle.nested'
       >>> getByDot(x,q)
       "value"
    """
    def gbd(obj,ref):
        val = obj
        tmp = ref
        ref = tmp.replace(".XX","[0]")
        if tmp != ref:
    #        print("Warning: replaced '.XX' with [0]-th index")
            pass
        for key in ref.split('.'):
            idstart = key.find("[")
            embedslist = 1 if idstart > 0 else 0
            if embedslist:
                idx = int(key[idstart+1:key.find("]")])
                kyx = key[:idstart]
                try:
                    val = val[kyx][idx]
                except IndexError:
                    print("Index: x['{}'][{}] does not exist.".format(kyx,idx))
                    raise
            else: 
                val = val[key]
        return(val)
    
    if strict:
        return(gbd(obj,ref))
    else:
        try:
            return(gbd(obj,ref))
        except:
            return('')



def connection_to_mong(database, collection='production', hostname='localhost', portnumber=27017):
    datab=database
    connection = pymongo.MongoClient(host=hostname, port=portnumber)
    db = getattr(connection, datab)
    
def index_mong(variablename):
    coll.ensure_index(variablename)

def count_for_list(listvariablename):
    list_mong = db.production.distinct(listvariablename)
    list_results = {}
    for i in list_mong:
        itemname = i
        listcount = db.production.find({listvariablename:itemname}).count()
        list_results[itemname] = listcount
    #print list_results
    return list_results

def count_nones_and_exists(variablename):
    numexists = db.production.find({variablename:{'$exists': 'true'}}).count()
    numnones = db.production.find({variablename: None}).count()
    numnonones = db.production.find({variablename:{'$ne': None}}).count()
    nonexcounts ={'number_of_values':numnonones, 'number_of_nulls': numnones, 'number_exists': numexists}
    #print nonexcounts
    return nonexcounts

def stats(variablename):
    stats = {}
    distinct_list = db.production.distinct(variablename)
    clean_numbers_list = []
    for i in distinct_list:
        number = float(i)
        clean_numbers_list.append(number)
    #mean_of_list = db.production.aggregate("")
    if None in clean_numbers_list:
        clean_numbers_list.remove(None)
    if clean_numbers_list != []:
        min_of_list = min(clean_numbers_list)
        max_of_list = max(clean_numbers_list) 
        mean_of_list = sum(clean_numbers_list)/len(clean_numbers_list)  
        stats['minimum_value'] = min_of_list
        stats['maximum_value'] = max_of_list
        stats['mean_value'] = mean_of_list
    else:
        stats = None
    return stats


all_variables = ["institution.description", "institution.characteristics", "institution.public_private", "institution.gender", "institution.academic_calendar", "institution.awards", "institution.student_teacher_ratio", "institution.admission.fee_amount", "institution.admission.defer", "institution.freshman_profile.SAT_submission_perc", "institution.freshman_profile.ACT_submission_perc", "institution.financial_aid.average_debt_at_graduation", "institution.religion_offer", "institution.religion.christian", "institution.religion.islamic", "institution.religion.jewish", "institution.religion.buddhist"]
list_count = ["institution.public_private", "institution.characteristics", "institution.religion_offer", "institution.gender", "institution.academic_calendar", "institution.awards", "institution.student_teacher_ratio", "institution.admission.defer"]
min_max_avg_count = ["institution.student_teacher_ratio", "institution.admission.fee_amount", "institution.admission.defer", "institution.freshman_profile.SAT_submission_perc", "institution.freshman_profile.ACT_submission_perc","institution.financial_aid.average_debt_at_graduation"]



def main():
    finaloutputdict = {}
    for variable in all_variables:
        count1, count2, count3 = None, None, None
        index_mong(variable)
        count1 = count_nones_and_exists(variable)
        #print count1
        if variable in list_count:
            count2 = count_for_list(variable)
        if variable in min_max_avg_count:
            count3 = stats(variable)
            #print count3
        finaloutputdict[variable] = (count1, count2, count3)
        #print finaloutputdict
    return finaloutputdict
          

if __name__ == "__main__":
    print main()







"""
def main():
    connection_to_mong(K12)
    for variable in all_variables:
        index_mong(variable)
    

#schools=coll.find()






if __name__ == "__main__":


"""
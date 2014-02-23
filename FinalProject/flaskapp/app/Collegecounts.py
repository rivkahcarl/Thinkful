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
from noodletricks import getByDot

database = 'postsecondary'
connection = pymongo.MongoClient(host="ec2-54-226-101-255.compute-1.amazonaws.com", port=27017)
db = getattr(connection,database)
coll=db['production']
#sys.exit(0)

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
    #mean_of_list = db.production.aggregate("")
    if None in distinct_list:
        distinct_list.remove(None)
    if distinct_list != []:
        min_of_list = min(distinct_list)
        max_of_list = max(distinct_list) 
        mean_of_list = sum(distinct_list)/len(distinct_list)  
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
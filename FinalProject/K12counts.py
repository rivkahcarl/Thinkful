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

database = 'K12'
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
    if None in distinct_list:
        distinct_list.remove(None)
    if distinct_list != []:
        min_of_list = min(distinct_list)
        max_of_list = max(distinct_list)
        mean_of_list = np.mean(distinct_list)
        stats['minimum_value'] = min_of_list
        stats['maximum_value'] = max_of_list
        stats['mean_value'] = mean_of_list
    else:
        stats = None
    return stats

all_variables = ["institution.school_type", "institution.school_type_display", "institution.publicprivate", "institution.publicprivate_display", "institution.school_level","institution.faculty_fte", "institution.grad_4year_prct", "institution.student_teacher_ratio", "institution.freereduced_lunch", "institution.avg_class_size"] #,  "institution.url", "institution.school_gender", "institution.grade_low", "institution.grade_high", "institution.email", "institution.phone", "institution.video", "institution.accreditation", "institution.associations", "institution.description", "institution.curriculum_description", "institution.extracurricular_description", "institution.teacher_description", "institution.discipline_description", "institution.health_description","institution.facilities_description", "institution.mission_statement", "institution.charter", "institution.magnet", "institution.finaid_titlei_school", "institution.activities.non_academic", "institution.activities.academic", "institution.special_needs_offer", "institution.special_needs.learning", "institution.special_needs.mental", "institution.special_needs.behavioral", "institution.special_needs.medical", "institution.special_needs.physical", "institution.religion_offer", "institution.religion.islamic", "institution.religion.jewish", "institution.religion.christian", "institution.religion.buddhist", "institution.sports.male", "institution.sports.female", "institution.endowment", "institution.dress_code", "institution.special_classes"]
list_count = ["institution.school_type", "institution.school_type_display", "institution.publicprivate", "institution.publicprivate_display", "institution.school_level"] #,  "institution.charter", "institution.magnet", "institution.accreditation", "institution.associations", "institution.activities.non_academic", "institution.activities.academic", "institution.special_needs_offer", "institution.special_needs.learning", "institution.special_needs.medical", "institution.special_needs.behavioral", "institution.special_needs.physical", "institution.religion.offer", "institution.religion.islamic", "institution.religion.jewish", "institution.religion.christian", "institution.religion.buddhist", "institution.sports.male", "institution.sports.female", "institution.special_classes"]
min_max_avg_count = ["institution.faculty_fte", "institution.grad_4year_prct", "institution.student_teacher_ratio", "institution.freereduced_lunch", "institution.avg_class_size"]



def main():
    finaloutputdict = {}
    for variable in all_variables:
        count1, count2, count3 = None, None, None
        index_mong(variable)
        count1 = count_nones_and_exists(variable)
        if variable in list_count:
            count2 = count_for_list(variable)
        if variable in min_max_avg_count:
            count3 = stats(variable)
            print count3
        #if variable in min_max_avg_count:
            #count_with_details_min(variable)
        finaloutputdict[variable] = (count1, count2, count3)
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
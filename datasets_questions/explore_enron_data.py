#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

file = open("../final_project/poi_names.txt", "r")
lines = file.read().split('\n')
names = []
for line in lines:
    if line[:3] == "(y)" or line[:3] == "(n)":
        names.append(line[4:].replace(",", "").lower())
print "names in text file: ", len(names)

features_max = poi_count = names_match = salary_count = email_count = total_payments_nan = total_payments_nan_poi = 0
people_count = len(enron_data)
for key in enron_data.keys():
    if len(enron_data[key]) > features_max:
        features_max = len(enron_data[key])
    if enron_data[key]["poi"]:
        poi_count += 1
    if not enron_data[key]["salary"]=="NaN":
        salary_count += 1
    if not enron_data[key]["email_address"]=="NaN":
        email_count += 1
    if enron_data[key]["total_payments"]=="NaN":
        total_payments_nan += 1
    if enron_data[key]["poi"] and enron_data[key]["total_payments"]=="NaN":
        total_payments_nan_poi += 1
#    if key.lower() in names:
#        names_match += 1
print "people count: ", people_count
print "features count: ", features_max
print "poi count: ", poi_count
#print "poi match: ", names_match
print "stock James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "messages Wesley Colwell: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "options Jeffrey Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "total Lay: ", enron_data["LAY KENNETH L"]["total_payments"]
print "total Skilling: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "total Fastow: ", enron_data["FASTOW ANDREW S"]["total_payments"]
print "salary count: ", salary_count
print "email count: ", email_count
print "total payments nan %: ", 100.0*total_payments_nan/people_count, " %"
print "total payments nan poi %: ", 100.0*total_payments_nan_poi/people_count, " %"
print "adding 10 pois with NaN total payment..."
people_count_new = people_count + 10
total_payments_nan_new = total_payments_nan + 10
poi_count_new = poi_count + 10
total_payments_nan_poi_new = total_payments_nan_poi + 10
print "new people count: ", people_count_new
print "new total payments nan: ", total_payments_nan_new
print "new poi count: ", poi_count_new
print "new total payments nan poi: ", total_payments_nan_poi_new
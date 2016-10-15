#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

'''
outlier = sorted(data, key=lambda x: x[0], reverse=True)[0]
print "outlier salary: ", outlier[0]
print "outlier bonus: ", outlier[1]
'''

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    if salary>1000000. and bonus>5000000.:
        print point
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



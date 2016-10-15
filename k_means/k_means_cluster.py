#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


def featureScaling(value, min, max):
    return (1.0*value-min)/(max-min)


def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)



min_eso = max_eso = -1
for key in data_dict.keys():
    eso = data_dict[key]["exercised_stock_options"]
    if eso == "NaN":
        continue
    if min_eso == -1:
        min_eso = max_eso = eso
    else:
        if min_eso > eso:
            min_eso = eso
        if max_eso < eso:
            max_eso = eso
print "exercised_stock_options min: ", min_eso
print "exercised_stock_options max: ", max_eso

min_sal = max_sal = -1
for key in data_dict.keys():
    sal = data_dict[key]["salary"]
    if sal == "NaN":
        continue
    if min_sal == -1:
        min_sal = max_sal = sal
    else:
        if min_sal > sal:
            min_sal = sal
        if max_sal < sal:
            max_sal = sal
print "salary min: ", min_sal
print "salary max: ", max_sal

min_fm = max_fm = -1
for key in data_dict.keys():
    fm = data_dict[key]["from_messages"]
    if fm == "NaN":
        continue
    if min_fm == -1:
        min_fm = max_fm = fm
    else:
        if min_fm > fm:
            min_fm = fm
        if max_fm < fm:
            max_fm = fm
print "from_messages min: ", min_fm
print "from_messages max: ", max_fm



for key in data_dict.keys():
    eso = data_dict[key]["exercised_stock_options"]
    if eso == "NaN":
        continue
    data_dict[key]["exercised_stock_options"] = featureScaling(eso, min_eso, max_eso)

for key in data_dict.keys():
    sal = data_dict[key]["salary"]
    if sal == "NaN":
        continue
    data_dict[key]["salary"] = featureScaling(sal, min_sal, max_sal)

for key in data_dict.keys():
    fm = data_dict[key]["from_messages"]
    if fm == "NaN":
        continue
    data_dict[key]["from_messages"] = featureScaling(fm, min_fm, max_fm)



print "rescaled salary: ", featureScaling(200000, min_sal, max_sal)
print "rescaled exercised_stock_options: ", featureScaling(1000000, min_eso, max_eso)



### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
#feature_2 = "exercised_stock_options"
feature_2 = "from_messages"
#feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
#features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
#for f1, f2, f3 in finance_features:
        plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans

clf = KMeans(n_clusters = 2)
clf.fit(finance_features)
pred = clf.predict(finance_features)

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"

#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


### your code goes here
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    features, labels, test_size=0.3, random_state=42)

from sklearn import tree
from sklearn.metrics import precision_score, recall_score

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
accuracy = clf.score(features_test, labels_test)
print "accuracy: ", accuracy

poi_count = 0
for poi in labels_test:
    if poi == 1.0:
        poi_count+=1
print poi_count
print "test size: ", len(features_test)

labels_test_fake = [0.0 for i in range(len(labels_test))]
match_count_fake = 0
for (real,fake) in zip(labels_test,labels_test_fake):
    if real==fake:
        match_count_fake+=1
accuracy_fake = 1.0 * match_count_fake / len(labels_test)
print "accuracy fake: ", accuracy_fake

precision_fake = precision_score(labels_test, labels_test_fake)
print "precision fake: ", precision_fake
recall_fake = recall_score(labels_test, labels_test_fake)
print "recall fake: ", recall_fake


pred_example = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_example = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
true_positives_count = true_negatives_count = false_positives_count = false_negatives_count = 0
for (pred,true) in zip(pred_example,true_example):
    if pred == 1:
        if true == 1:
            true_positives_count+=1
        elif true == 0:
            false_positives_count+=1
    elif pred == 0:
        if true == 1:
            false_negatives_count+=1
        elif true == 0:
            true_negatives_count+=1
print "true positives: ", true_positives_count
print "true negatives: ", true_negatives_count
print "false positives: ", false_positives_count
print "false negatives: ", false_negatives_count

precision_example = precision_score(true_example, pred_example)
print "precision example: ", precision_example
recall_example = recall_score(true_example, pred_example)
print "recall example: ", recall_example
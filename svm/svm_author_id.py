#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score

#cs = [1., 10., 100., 1000., 10000.]
cs = [10000.]
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

for i in cs:
    clf = svm.SVC(kernel='rbf', C=i)
    print
    print i

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time: ", round(time()-t0, 3), "s"

    t1 = time()
    prediction = clf.predict(features_test)
    print "prediction time: ", round(time()-t1, 3), "s"

    print "10th element: ", prediction[10]
    print "26th element: ", prediction[26]
    print "50th element: ", prediction[50]

    sara = chris = 0
    for j in prediction:
        if j==1:
            chris+=1
        else:
            sara+=1
    print "0 sara: ", sara
    print "1 chris: ", chris

    accuracy = accuracy_score(prediction, labels_test)
    print "accuracy: ", accuracy
#########################################################



#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    ### your code goes here
    length = len(predictions)
    helper = []
    for i in range(length):
        helper.append([ (predictions[i]-net_worths[i])**2, i ])
    helper.sort()
    cleaned_data = []
    reduced = int(length*0.9)
    for i in range(reduced):
        index = helper[i][1]
        cleaned_data.append((ages[index], net_worths[index], predictions[index]-net_worths[index]))
    return cleaned_data


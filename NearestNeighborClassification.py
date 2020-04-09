#Maddie Pero 
#Step 2 & 3 project 2

import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS

#this function opens the csv file of data, reads it and then normalizes the data for glucose and hemoglobin
#it takes no arguments 
#it returns the scaled glucose data, the scaled hemoglobin data, and the classifier data in numpy arrays 
def readDataFile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    glucoseScaled = ((glucose - 70 )/ (490- 70))
    hemoglobinScaled = ((hemoglobin - 3.1)/(17.8 - 3.1))
    return glucoseScaled, hemoglobinScaled, classification

#this function creates a random test case for hemoglobin and glucose between 0 and 1
#it takes no arguments
#it returns the test case of hemoglobin and glucose as integeters
def TestCase():
    array = np.random.rand(2,1)
    newhemoglobin = array[0]
    newglucose = array[1]
    return newhemoglobin, newglucose

#this functions graphs the scaled hemoglobina and glucose data, and colors each point based on its classification
#it takes 3 arguments the numpy arrays of data for glucose, hemoglobin, and classification
#it returns the plot of the data
def graphData(glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.title('Glucose vs. Hemoglobin of Patients')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    return plt.show()

#this function calclautes the distance from each point to the random rest case
#it takes 4 arguments, two integers (newglucose and newhemoglobin) which are the test case, and 2 arrays which are the hemoglobin and glucose data from the csv file 
#it returns a numpy array that has all the distances from each point to the test case 
def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    distanceArray = np.array(np.sqrt(((glucose - newglucose)**2) + ((hemoglobin - newhemoglobin)**2)))
    return distanceArray

#this function finds the nearest neighbor to the test case and then determines the class of the test case
#it takes 5 arguments, two integers (newglucose and newhemoglobin) which are the test case, and 3 arrays which are the hemoglobin, glucose and classification data from the csv file
#it returns an integer that is the class of the test case
def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distanceArray = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    min_index = np.argmin(distanceArray)
    nearest_class = classification[min_index]
    return nearest_class

#this function graphs the test case as well as everything from the function graphData()
#it takes 5 arguments, two integers (newglucose and newhemoglobin) which are the test case, and 3 arrays which are the hemoglobin, glucose and classification data from the csv file
#it returns the plot that is the graph of all the data & the test case
def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot(newhemoglobin[nearest_class==1],newglucose[nearest_class==1], "k.", markersize = 17, label = "Test Case")
    plt.plot(newhemoglobin[nearest_class==0],newglucose[nearest_class==0], "r.", markersize = 17, label = "Test Case")
    plt.title('Glucose vs. Hemoglobin of Patients')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    return plt.show()

#this function uses k nearest neighbor classifier to find the classification of the test case based on k number of points around it 
#it takes 6 arguments, 3 integers newglucose and newhemoglobin which are the test case and k which is the of number of neighbors, and 3 arrays which are the hemoglobin, glucose and classification data from the csv file
#it returns the class of the test case
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distanceArray = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    sorted_indices = np.argsort(distanceArray)
    k_indices = sorted_indices[:k]
    k_classification = classification[k_indices]
    k_class = np.median(k_classification)
    return k_class
    
# MAIN SCRIPT
    
glucose, hemoglobin, classification = openckdfile()
newhemoglobin, newglucose = TestCase()
nearest_class = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
graphData(glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
k_class = kNearestNeighborClassifier(3, newglucose, newhemoglobin, glucose, hemoglobin, classification)
print("Class from K-Nearest Neighbor: " + str(k_class) )
print("Class from Nearest Neighbor: " + str(nearest_class) )
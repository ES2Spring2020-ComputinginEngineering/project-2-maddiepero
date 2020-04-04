#Maddie Pero 
#Step 2 & 3 project 2

import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    glucoseScaled = ((glucose - 70 )/ (490- 70))
    hemoglobinScaled = ((hemoglobin - 3.1)/(17.8 - 3.1))
    return glucoseScaled, hemoglobinScaled, classification

def TestCase():
    array = np.random.rand(2,1)
    newhemoglobin = array[0]
    newglucose = array[1]
    return newhemoglobin, newglucose

def graphData():
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    return plt.show()

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    distanceArray = np.array(np.sqrt(((glucose - newglucose)**2) + ((hemoglobin - newhemoglobin)**2)))
    return distanceArray

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distanceArray = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    min_index = np.argmin(distanceArray)
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot(newhemoglobin[nearest_class==1],newglucose[nearest_class==1], "k.", markersize = 17)
    plt.plot(newhemoglobin[nearest_class==0],newglucose[nearest_class==0], "r.", markersize = 17)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    return plt.show()

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distanceArray = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    sorted_indices = np.argsort(distanceArray)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    k_class = np.median(k_classifications)
    return k_class
    
# MAIN SCRIPT
    
glucose, hemoglobin, classification = openckdfile()
newhemoglobin, newglucose = TestCase()
nearest_class = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
graphData()
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)

k_class = kNearestNeighborClassifier(3, newglucose, newhemoglobin, glucose, hemoglobin, classification)

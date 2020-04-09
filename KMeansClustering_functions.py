#Maddie Pero
#Project 2 Step 4 Functions

#import statements
import numpy as np
import matplotlib.pyplot as plt
import random

#global variables

#functions

#this function opens the ckd file, reads its data, and then normalizes its data
#it takes no arguments
#it returns three numpy arrays that are the normalized glucose, hemoglobin, and classification data
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    glucoseScaled = ((glucose - 70 )/ (490- 70))
    hemoglobinScaled = ((hemoglobin - 3.1)/(17.8 - 3.1))
    return glucoseScaled, hemoglobinScaled, classification

#this function randomly creates k number of centroids to intialize the K means algorithm
#it takes one argument an integer k which is the number of clusters the programer desires the algorithm to use 
#it returns a numpy array that is the randomly crated centroids
def Initialize(k):
    glucoseScaled, hemoglobinScaled, classification = openckdfile()
    centroids = array = np.random.rand(k,2)
    return centroids

#this function assigns each data point to a cluster based on what centroid they are closest too
#it takes two arguments an integer k which is the number of clusters the programer desires the algorithm to use and the array of centroids 
#it returns a numpy array of the assignments 
def Assign(k, centroid):
    glucoseScaled, hemoglobinScaled, classification = openckdfile()
    distanceArray = np.zeros((158, k))
    for i in range(k):
        distanceArray1 = np.array(np.sqrt(((glucoseScaled - centroid[i,0])**2) + ((hemoglobinScaled - centroid[i,1])**2)))
        distanceArray[:,i] = distanceArray1
    assignment = np.zeros(158)
    for i in range(158):
        min_index = np.argmin(distanceArray[i])
        assignment[i] = min_index
    return assignment

#this function update the centroids based on the averages of data points assigned to that cluster
#it takes two arguments k which is the numer of clusters the programer desires the algorithm to use and the array of assignments
#it returns an array of updates centroids 
def Update(k, assignment):
    glucoseScaled, hemoglobinScaled, classification = openckdfile()
    new_centroid = np.zeros((k,2))   
    for x in range(k):
        glucose_to_average = np.zeros((1))
        hemoglobin_to_average = np.zeros((1))
        assignment_to_average, = np.where(assignment == x)
        for i in assignment_to_average:
            glucose_to_average = np.append(glucose_to_average, [glucoseScaled[i]])
            hemoglobin_to_average = np.append(hemoglobin_to_average, [hemoglobinScaled[i]])
        new_centroid[x:,1] = np.average(glucose_to_average)
        new_centroid[x:,0] = np.average(hemoglobin_to_average)
    return new_centroid

#this function makes the algorithm run over and over again until a certain end case is met
#it takes two arguments k whcih is the number of clusters the programer desires the algorithm to use and max_iterations which is the number of times the programer wants the algorithm to run
#it returns the final centroids and assignment arrays
def Iterate(k, max_iterations):
    centroid = Initialize(k)
    for i in range(max_iterations):
        assignment = Assign(k, centroid)
        centroid = Update(k, assignment)
    return centroid, assignment
    
#this function graphs the data from the ckd file in its appropriate clusters
#it rakes 4 arrays that are the glucose, hemoglobin, assignment, and centroid data
#it is a void function
def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    plt.figure()
    for i in range(int(np.amax(assignment)) + 1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
 
#this function calculates the percents for true positives, false positives, ture negatives, and false negatives of the K means algorithm 
#it takes two arguments the numpy arrays for classifications from the ckd file and assignments from the k means algorithm
#it is a void function
def Percent_Calc(classifcations, assignment):
    true_pos = 0
    false_pos = 0
    true_neg = 0
    false_neg = 0
    CKD = 0
    Non_CKD = 0 
    for i in range(158):
        if classifcations[i] == assignment[i] == 1:
            true_neg += 1 
            Non_CKD += 1
        elif classifcations[i] == 0 and assignment[i] == 1:    
            false_neg += 1
            CKD += 1
        elif classifcations[i] == assignment[i] == 0:
            true_pos += 1
            CKD += 1
        elif classifcations[i] == 1 and assignment[i] == 0:
            false_pos += 1
            Non_CKD += 1
    
    print("Rate of True Positives: " + str((true_pos/CKD)*100) + ' %')         
    print("Rate of False Positives: " + str((false_pos/Non_CKD)*100) + ' %')
    print("Rate of True Negatives: " + str((true_neg/Non_CKD)*100) + ' %') 
    print("Rate of False Negatives: " + str((false_neg/CKD)*100) + ' %') 

#main srip


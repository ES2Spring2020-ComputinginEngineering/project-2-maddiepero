#Maddie Pero
#Project 2 Step 4 Driver

#import statements
import KMeansClustering_functions as kmc #Use kmc to call your functions

#global variables

#custom functions

#main script 
k = 3
glucose, hemoglobin, classifications = kmc.openckdfile()
centroids, assignment = kmc.Iterate(k, 1000)
kmc.graphingKMeans(glucose, hemoglobin, assignment, centroids)
kmc.Percent_Calc(classifications, assignment) 

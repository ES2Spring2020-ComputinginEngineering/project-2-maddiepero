This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Maddie Pero
Project 2 Readme

Directions for using NearestNeighborClassification.py:

	To use this code simply run the file. It will produce two graphs. One without the test case and another with a test case 
	that will have a classifcation that is identifiable by the color the dot is graphed in. The file will also print the class 
	as identified by the K-Nearest Neighbor and Nearest Neighbor functions. If you wish to use a different csv file with the same
	type of data simply replace the file name in the readData function and then run the file. 

Directions for using KMeansClustering_Driver.py:

	To use this file simply select the number of clusters desired in the algorithm by changing the number the varible k is equal to 
	in the main script then run. The file will automatically calculate and print the rates of true positives, true negatives, false positives, and
	false negatives even though the Percent_Calc function is only meant for a k=2 algorithm. If you do not wish it to print for k=1 and k=3 comment out 
	line 16. This file will also print a graph that shows the clusters by color and the centroids indicated by a larger shape. 

Directions for using KMeansClustering_Functions.py:

	Do not use this file in any capacity other than running it in KMeansClustering_driver.py file. It only contains functions. There is not main script
	and it will not print anything. 

Function overview for KMeansClustering_Functions.py:

	opencdkfile() :
	this function opens the ckd file, reads its data, and then normalizes its data
	it takes no arguments
	it returns three numpy arrays that are the normalized glucose, hemoglobin, and classification data
	
	Initialize(k) :
	this function randomly creates k number of centroids to intialize the K means algorithm
	it takes one argument an integer k which is the number of clusters the programer desires the algorithm to use 
	it returns a numpy array that is the randomly crated centroids

	Assign(k, centroid) :
	this function assigns each data point to a cluster based on what centroid they are closest too
	it takes two arguments an integer k which is the number of clusters the programer desires the algorithm to use and the array of centroids 
	it returns a numpy array of the assignments 

	Update(k, assignment):
	this function update the centroids based on the averages of data points assigned to that cluster
	it takes two arguments k which is the numer of clusters the programer desires the algorithm to use and the array of assignments
	it returns an array of updates centroids 

	Iterate(k, max_iterations):
	this function makes the algorithm run over and over again until a certain end case is met
	it takes two arguments k whcih is the number of clusters the programer desires the algorithm to use and max_iterations which is the number of times
	the programer wants the algorithm to run
	it returns the final centroids and assignment arrays

	graphingKMeans(glucose, hemoglobin, assignment, centroids):
	this function graphs the data from the ckd file in its appropriate clusters
	it rakes 4 arrays that are the glucose, hemoglobin, assignment, and centroid data
	it is a void function

	Percent_Calc(classifications, assignment):
	this function calculates the percents for true positives, false positives, ture negatives, and false negatives of the K means algorithm 
	it takes two arguments the numpy arrays for classifications from the ckd file and assignments from the k means algorithm
	it is a void function
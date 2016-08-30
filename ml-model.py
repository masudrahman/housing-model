import numpy
import csv
import math

'''
Cost function
@param input {matrix} 
@param output {matrix}
@param theta {matrix}
'''
def costFunction(inputX, outputY, theta):
	J = math.pow(sum((inputX*theta)-outputY),2)
	J = J/(2 * len(inputX))
	return J


# initialize theta to zeros
theta = numpy.matrix(str(0) + ';' + str(0))

# initialize feature matrix and output matrix from datapoints of csv file
feature_matrix = []
output_matrix = []

with open('cleanData.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)

	for row in reader:
		if (row[0] == 'SQFT'):
			continue
		feature_matrix.append([1,int(row[0])])
		output_matrix.append([int(row[1])])

	feature_matrix = numpy.matrix(feature_matrix)
	output_matrix = numpy.matrix(output_matrix)

costFunction(feature_matrix, output_matrix, theta)
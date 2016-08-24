import numpy
import csv

# initialize theta to zeros
theta = numpy.matrix(str(0) + ';' + str(0))

with open('cleanData.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)

	feature_matrix = []

	for row in reader:
		if (row[0] == 'SQFT'):
			continue
		feature_matrix.append([1,int(row[0])])

	print numpy.matrix(feature_matrix)
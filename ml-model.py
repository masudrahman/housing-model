import numpy
import csv

with open('redfin_2016-08-22-23-01-42_results.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print row
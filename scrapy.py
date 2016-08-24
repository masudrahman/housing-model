import csv

arr = []

'''
	Clean the data from the csv file to sqft and price
'''
with open('redfin_2016-08-22-23-01-42_results.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)

	with open('cleanData.csv', 'wb') as cleanCSV:
		writer = csv.writer(cleanCSV)

		for row in reader:
			if (len(row[10]) != 0):
				writer.writerow( (row[10], row[6]) )
			else:
				continue
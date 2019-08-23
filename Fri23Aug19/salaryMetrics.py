#!/usr/bin/python3

import csv
import math
# import pandas as pd

csvPath = './salaries.csv'
columnNum = 2

n = 0
total = 0
maxSalary = 0

# for chunk in pd.read_csv(csvPath, chunksize = 10000000):
# 	chunkTotal = chunk.iloc[:, columnNum].sum()
# 	total += chunktotal


# Get average and max of column 3
with open(csvPath) as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	next(csvReader) # to skip header line
	for row in csvReader:
		n += 1
		salary = float(row[columnNum])
		total += salary
		if salary > maxSalary:
			maxSalary = salary

sampleMean = total / n

sumDifferencesSquared = 0
minSalary = maxSalary
salary = 0
# Get stdev and min of column 3
with open(csvPath) as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	next(csvReader) # to skip header line
	for row in csvReader:
		salary = float(row[columnNum])
		sumDifferencesSquared += (salary - sampleMean)**2
		if salary < minSalary:
			minSalary = salary

standardDeviation = math.sqrt(sumDifferencesSquared/(n-1))

print('Sample Mean: ', sampleMean)
print('Sample Standard Deviation: ', standardDeviation)
print('Max Salary: ', maxSalary)
print('Min Salary', minSalary)


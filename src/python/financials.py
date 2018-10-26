#list of dates: "ember-view-ui-sortable"

import csv
import sys
import cik
from pandas import DataFrame
import pandas as pd

def getReport(cik, year, quarter):
	#use asdh not cik, you fucked up, also get suptype, and company name, and anything else useful from sub while ur at it

	compiled1 = []

	compiled2 = []

	index = True
	with open('Financials/QuarterlyStatements/' + str(year) + 'q' + str(quarter)+ '/sub.txt', newline='\n') as csvfile:
	   csvreader = csv.reader(csvfile, delimiter='\t')
	   for row in csvreader:
	   	if index:
	   		headers = row
	   		index = False
	   	if(row[1] == cik):
	   		compiled1.append(row)


	data1 = DataFrame(compiled1, columns=headers)
	print(data1)
	listadsh = data1['adsh']

	headers2 =[]
	index=True
	with open('Financials/QuarterlyStatements/' + str(year) + 'q' + str(quarter)+ '/num.txt', newline='\n') as csvfile:
	    csvreader = csv.reader(csvfile, delimiter='\t')
	    for row in csvreader:
	    	#print(row[0])
	    	if index:
	    		headers2 = row
	    		index = False
	    	for adsh in listadsh:
	    		if(row[0] == adsh):
	    			compiled2.append(row)
	print(compiled2)
	print(headers)
	data2 = DataFrame(compiled2, columns=headers2)
	print(data2)
	    #data = data.sort_values(['ddate','tag'], ascending=False)
	    #print(data)

		#data.drop_duplicates(subset=data['tag'],keep=first, inplace = False)
	    #writer = pd.ExcelWriter('output.xlsx') #check full output
	    #data.to_excel(writer,'Sheet1')
	    #writer.save()
	    #print(compiled)
	return data2


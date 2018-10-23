#list of dates: "ember-view-ui-sortable"

import csv
import sys
import cik
from pandas import DataFrame
import pandas as pd

def getReport(cik, year, quarter):
	while len(cik) < 10:
		cik= '0' + cik
	compiled = []
	index = True
	with open('Financials/QuarterlyStatements/' + str(year) + 'q' + str(quarter)+ '/num.txt', newline='\n') as csvfile:
	    csvreader = csv.reader(csvfile, delimiter='\t')
	    for row in csvreader:
	    	if index:
	    		headers = row
	    		index = False
	    	if(row[0].split('-')[0] == cik):
	    		compiled.append(row)
	    data = DataFrame(compiled, columns=headers)
	    data = data.sort_values(['ddate','tag'], ascending=False)
	    #print(data)
	    writer = pd.ExcelWriter('output.xlsx') #check full output
	    data.to_excel(writer,'Sheet1')
	    writer.save()
	    #print(compiled)
	    return data


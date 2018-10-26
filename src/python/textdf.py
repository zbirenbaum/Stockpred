import earnings
import news
import datetime
import cik
import financials
import pandas as pd
import subtype
import simplejson
import json
import sys
import numpy as np
import os
from pathlib import Path
import csv


def toFrame():
	listyears = ['2018']
	listquarters = ['4','3','2','1']
	compiled1 = []
	ticker = 'AAPL'
	ciknum = cik.tickerLookup(ticker)
	for year in listyears:
		for quarter in listquarters:
			print(quarter)
			index = True
			file = Path('Financials/QuarterlyStatements/' + str(year) + 'q' + str(quarter)+ '/sub.txt')
			if(file.is_file()):
				with open('Financials/QuarterlyStatements/' + str(year) + 'q' + str(quarter)+ '/sub.txt', newline='\n') as csvfile:
					csvreader = csv.reader(csvfile, delimiter='\t')
					for row in csvreader:
						#print(row)
						if index:
					   		headers = row
					   		index = False

						if(row[1] == ciknum):
					   		compiled1.append(row)

	print(len(compiled1))
	with open(ticker + 'csv', 'w') as f:
	    for sublist in compiled1:
	        for item in sublist:
	            f.write(item + ',')
	        f.write('\n')

toFrame()


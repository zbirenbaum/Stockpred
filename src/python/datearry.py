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

def getDateArray(data, dropdup, ticker):
	dates = [] # holds all years
	rows = []
	listbody = []

	for row in (data.iterrows()):
		listbody.append(row[1])
		##dates.append(row[1]['ddate'][:4])
	#print(rows)
	#print(data.index)

	emptylist = []
	data2 = []
	ticker=ticker
	tag = {}
	counter = 1
	headerlist = {}
	header = 0
	dropdup = list(dropdup)
	for tags in dropdup:
		templist = []
		emptylist = []
		data2 = []
		header = 0
		headerlist = {}
		for rows in listbody:
			templist = []
			data2 = []
			if rows['tag'] == tags:
				#headerlist.append(str(header) )
				header = header + 1
				blanklist = []
				for i in range(0,8):
					if i != 3:
						templist.append(str(data.columns[i]))
						blanklist.append(rows.tolist()[i])
						#templist.append(data2)
						data2 = []
				todict = { j : blanklist[templist.index(j)] for j in templist}
				headerlist.update({header:todict})
		tag[tags] = (headerlist)



		
	values=data.columns

	heirarchy = [ticker, tag]
	templist = []
	nums = [0]
	data = []

	tree = {}
	
	tree[ticker] = tag
	#tree.append(tag)
	#tree.append(ticker)
	#tree[0] = []

	"""
	pritn(tree)

	#counter = 0

	for tags in tag:
		tree[0].append(tags)
		tree[0][counter] = []
		templist=[]
		for rows in listbody:
			if rows['tag'] == tag[counter]:
				for i in range(0,8):
					templist.append(str(data.columns[i])  +  rows.tolist()[i])

				tree[0][counter].append(templist)

				print(rows.tolist())
		counter = counter+1

	"""


	#print(tree)
	with open("dataFile.json", "w") as dataFile:
		string = simplejson.dumps(tree, indent=4, sort_keys=False)
		string.replace(']:', ']')

		dataFile.write(string)
	dataFile.close()

def formatJson():
	print("todo")



data = financials.getReport('320193', "2018", "3")
dropdup = set(data['tag'])
print(dropdup)
listtags = list(dropdup)

getDateArray(data, dropdup, "AAPL")


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

def getDateArray(data, dropdup, ticker, year, quarter):
	dates = [] # holds all years
	rows = []
	listbody = []

	for row in (data.iterrows()):
		listbody.append(row[1])
		##dates.append(row[1]['ddate'][:4])
	#print(rows)
	#print(data.index)
	#todo: populate list of dates and iterate data backwords to get most recents? or keep as qtr and get report type?
	emptylist = []
	data2 = []
	ticker=ticker
	tag = {}
	counter = 1
	headerlist = {}
	header = 0
	dropdup = list(dropdup)
	print(dropdup)
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
				headerlist.update({todict['ddate'] + "-" + todict['qtrs']:todict})
		tag[tags] = (headerlist)



		
	values=data.columns

	heirarchy = [ticker, tag]
	templist = []
	nums = [0]
	data = []

	tree = {}
	print(tag)
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
	#with open('C:\\Users\\Zach\\Documents\\GitHub\\Stockpred\\src\\python\\Financials\\JSON\\' + year+ "Q" + quarter + "\\" + ticker +".json"), "w+") as dataFile:
	with open(ticker +".json", "w") as dataFile:
		string = simplejson.dumps(tree, indent=4, sort_keys=False)
		string.replace(']:', ']')

		dataFile.write(string)
	dataFile.close()

def formatJson():
	print("todo")




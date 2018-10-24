import earnings
import news
import datetime
import cik
import financials
import pandas as pd
import subtype
import simplejson
#import datearry
#currenttime = datetime.datetime.now()
#day = currenttime.strftime("%Y/%m/%d")
day="10/22/18"
ticker = 'AAPL'
year = "2018"
cik = cik.tickerLookup(ticker)
#print(cik)
data = financials.getReport('320193', "2018", "3")
print(data.columns)



values = []

dropdup = set(data['tag'])
#print(dropdup)
#listtags = list(dropdup) #list of tags w/o dup

toappend = []
rows = []
tagdata = []

"""
dates = []
for row in (data.iterrows()):
	rows.append(row)
	row[1].rename(row[1]['ddate'][:4])
	dates.append(row[1]['ddate'][:4])
	if row[1]['tag'] == "ComprehensiveIncomeNetOfTax":
		print(row)
""
#print(type(dateset[0]))
#print(dateset)

#grouping[next(data.iterrows())[1]['ddate'][:4]] = next(data.iterrows())[1]
print(grouping)
#print(list(table))
#print(type(listtags[1]))

for tags in listtags:
	for row in rows:
		if row[1]['tag'] == tags:
			if [row][1]['ddate'][:4]
			print(row[1]['ddate'][:4])
			grouping[row[1]['ddate'][:4]].append(row[1])

print(grouping)

"""

"""
for tags in listtags:
	#if tags == "ComprehensiveIncomeNetOfTax":
		#print("found")
	toappend = []
	lastyear = []
	curryear = []
	grouping = grouping.iloc[0:0]
	grouping = pd.DataFrame(columns=dateset)
	for row in rows:
		if row[1]['tag'] == tags:
			grouping[row[1]['ddate'][:4]].append(row[1])
		toappend = grouping
		print(toappend)
	table[tags] = toappend.to_json()

dataFile = open("dataFile.json", "w")

dataFile.write(simplejson.dumps(simplejson.loads(table.to_json()), indent=4, sort_keys=False)) #later for db
dataFile.close()
"""
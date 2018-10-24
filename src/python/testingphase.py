import earnings
import news
import datetime
import cik
import financials
import pandas as pd
import subtype
import simplejson
#currenttime = datetime.datetime.now()
#day = currenttime.strftime("%Y/%m/%d")
day="10/22/18"
ticker = 'AAPL'



cik = cik.tickerLookup(ticker)
print(cik)
data = financials.getReport('320193', "2018", "3")
dates = []
values = []
for value in data['value']:
	values.append(value)
for date in data['ddate']:
	dates.append(date)

table = pd.DataFrame()
tagdata = []

dropdup = set(data['tag'])
print(dropdup)
listtags = list(dropdup)
toappend = []
rows = []

for row in (data.iterrows()):
	rows.append(row)

print(type(listtags[1]))

for tags in listtags:
	toappend = []
	for item in rows:
		if item[1]['tag'] == tags:
			toappend.append(item[1])
	table[tags] = pd.Series(toappend)

dataFile = open("dataFile.json", "w")
dataFile.write(simplejson.dumps(simplejson.loads(table.to_json()), indent=4, sort_keys=False)) #later for db
dataFile.close()


	#list(values), list(date)], 
#newtable = pd.DataFrame(columns=[data['tag']])
#newtable = data.set_index('tag').T #change tag to columns





#getasdh = next(newtable.iterrows())[2]
#listtype = []
#for asdh in getasdh:
	#listtype.append(subtype.getSubType(cik, asdh)) works
#print(listtype)
#df2 = pd.DataFrame([listtype], columns=list(data['tag']))
#newtable.append(df2)
#drop columns keep last(most recent)

"""
dropdup = set(data['tag'])
print(dropdup)
listtags = list(dropdup)
combined = pd.DataFrame(columns=dropdup)
getdataforttag = next(data.iterrows())
row1 = ''
tag1 = ''
for row in getdataforttag:
	row1 = str(row[2])
	for tag in listtags:
		tag1 = str(tag)
		if row1 == tag1:
			combined[tag].append(row)

"""

#dataFile = open("dataFile.json", "w")
#dataFile.write(simplejson.dumps(simplejson.loads(combined.to_json()), indent=4, sort_keys=False)) #later for db
#dataFile.close()


#print(data.to_json())
#dataFile.write(simplejson.dumps(simplejson.loads(data.to_json()), indent=4, sort_keys=False)) #later for db
#dataFile.close()
#print(df2)
#writer = pd.ExcelWriter('output.xlsx') #check full output
#newtable.to_excel(writer,'Sheet1')
#writer.save()

#print(newtable)
#print(newtable)

#articleUrls = news.getNews(ticker, day)
#print(articleUrls)
#keywords = news.sigWords(articleUrls[0])
#dateRevQuarterly = earnings.getDateRevQuarterly("AAPL") #kinda slow tbh
#print(dateRevQuarterly)



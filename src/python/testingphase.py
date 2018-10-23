import earnings
import news
import datetime
import cik
import financials
import pandas as pd
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
	#list(values), list(date)], 
#newtable = pd.DataFrame(columns=[data['tag']])
newtable = data.set_index('tag').T #change tag to columns
writer = pd.ExcelWriter('output.xlsx') #check full output
newtable.to_excel(writer,'Sheet1')
writer.save()

print(newtable)
#print(newtable)

#articleUrls = news.getNews(ticker, day)
#print(articleUrls)
#keywords = news.sigWords(articleUrls[0])
#dateRevQuarterly = earnings.getDateRevQuarterly("AAPL") #kinda slow tbh
#print(dateRevQuarterly)



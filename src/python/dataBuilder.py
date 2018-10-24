import earnings
import news
import datetime
import cik
import financials
import pandas as pd
import subtype
import simplejson
import datearry


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


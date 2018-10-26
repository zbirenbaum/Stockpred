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


#print(cik)


year='2018'
quarter='3'
tickerlist = cik.getTickerList()
counter = 0
ticker = 'AAPL'

#data = financials.getReport(cik.tickerLookup(ticker), year, quarter)
data = financials.getReport(cik.tickerLookup(ticker), year, quarter)
dropdup = set(data['tag'])
listtags = list(dropdup)
datearry.getDateArray(data, dropdup, ticker, year, quarter)

counter = counter+1





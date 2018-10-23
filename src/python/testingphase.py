import earnings
import news
import datetime
import cik
import financials

#currenttime = datetime.datetime.now()
#day = currenttime.strftime("%Y/%m/%d")
day="10/22/18"
ticker = 'AAPL'



cik = cik.tickerLookup(ticker)
print(cik)
data = financials.getReport('320193', "2018", "3")
#articleUrls = news.getNews(ticker, day)
#print(articleUrls)
#keywords = news.sigWords(articleUrls[0])
#dateRevQuarterly = earnings.getDateRevQuarterly("AAPL") #kinda slow tbh
#print(dateRevQuarterly)



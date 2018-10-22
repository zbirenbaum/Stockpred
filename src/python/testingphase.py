import earnings
import news
import datetime

currenttime = datetime.datetime.now()
day = currenttime.strftime("%Y/%m/%d")
ticker = 'AAPL'




articleUrls = news.getNews(ticker, day)
#print(articleUrls)
keywords, summary = news.sigWords(articleUrls[0])
print(keywords)
print(summary)
#dateRevQuarterly = earnings.getDateRevQuarterly("AAPL")
#print(dateRevQuarterly)



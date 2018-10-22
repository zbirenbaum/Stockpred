import earnings
import news
import datetime

currenttime = datetime.datetime.now()
day = currenttime.strftime("%Y/%m/%d")
ticker = 'AAPL'




articleUrls = news.getNews(ticker, day)
print(articleUrls)
for url in articleUrls:
	print(news.getBody(url))
#dateRevQuarterly = earnings.getDateRevQuarterly("AAPL")
#print(dateRevQuarterly)



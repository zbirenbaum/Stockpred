from newsapi.newsapi_client import NewsApiClient
from dateutil.parser import parse
from datetime import datetime, timedelta
from newspaper import Article
import sys
import json
import requests
from numpy import array
import numpy as np
import json
import time
import nltk





#Init
api = NewsApiClient(api_key='625cab7a9f8740d98b1dd97496894f3f')


#get user input based on what's on search box and what's on 



def getNews(ticker, day):
    articleUrls = []
    formatDay = parse(day) #Current Day
    getArticles = api.get_everything(q=ticker,
                                        from_param=str(formatDay),
                                        to=str(formatDay),
                                        language='en',
                                        sources='abc-news, associated-press, australian-financial-review, bbc-news, bloomberg, business-insider, bussiness-insider-uk, cnbc, cnn, financial-times, financial-post, fortune, nbc-news, newsweek, the-economist, the-new-york-times, time, usa-today',                                       
                                        sort_by='popularity',
                                        )
    for i in getArticles['articles']:
        if (ticker in i["title"]):
            articleUrls.append(i['url'])


    return articleUrls



def getBody(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        body = article.text
    except:
        body='N/A'
    return body
def sigWords(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.keywords, article.summary





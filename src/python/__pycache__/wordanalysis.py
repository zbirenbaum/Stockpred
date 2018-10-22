from newsapi.newsapi_client import NewsApiClient
from dateutil.parser import parse
from datetime import datetime, timedelta
from newspaper import Article
from aylienapiclient import textapi
import sys
import json
import requests
from alpha_vantage import *
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from numpy import array
import numpy as np
import json
from sklearn import preprocessing
import time
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.feature_extraction.text import TfidfVectorizer


def getData(ticker):
	ts = TimeSeries(key=avkey, output_format = 'pandas')
	data, meta_data = ts.get_daily(ticker) #outputsize='full'
	popen = data['1. open']
	pclose = data['4. close']
	pdiff = pclose-popen
	return popen, pclose, pdiff

def calculations(series):
	mean = pop.mean()
	median = series.median()
	maxval = series.max()
	minval = series.min()
	standarddev = series.std()

def tfidf(totalnews):
	body = [totalnews]
	vectorizer = create_vectorizer(body)
	result = vectorizer.fit_transform(body)
	return result, vectorizer

def create_vectorizer(body):
    return TfidfVectorizer(input=body, stop_words='english')
                          

def scores(result, vectorizer):
    scores = zip(vectorizer.get_feature_names(),
                 np.asarray(result.sum(axis=0)).ravel())
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for item in sorted_scores:
        print("{0:50} Score: {1}".format(item[0], item[1]))

def getMaxValue(thisList):
	return thisList.index(max(thisList))

def getMinValue(list):
	return thisList.index(min(thisList))	

def getMaxKey(thisList):
	return thisList.index[getMaxValue(thisList)]

def getMinKey(list):
	return thisList.index[getMMinValue(thisList)]



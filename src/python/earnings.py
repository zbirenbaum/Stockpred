from selenium import webdriver
from bs4 import BeautifulSoup
import os    
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd

#look at newspaper nlp

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

"""
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.


driver=webdriver.Chrome(executable_path="C:/Users/Zach/Desktop/Stockpred/chromedriver.exe", chrome_options = options)
driver.get("https://ycharts.com/companies/AAPL/events/#/?eventTypes=earnings,&pageNum=1")
soup = BeautifulSoup(driver.page_source,"lxml")
driver.quit()
for item in soup.find_all(class_="colDate"):
    print(item
"""
def getDateRevQuarterly(ticker):
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')  # Last I checked this was necessary.


	driver=webdriver.Chrome(executable_path="C:/Users/Zach/Documents/GitHub/Stockpred/src/python/chromedriver.exe", chrome_options = options)
	driver.get("https://www.zacks.com/stock/chart/" + ticker+ "/fundamental/revenue-quarterly")
	soup = BeautifulSoup(driver.page_source,"lxml")
	driver.quit()
	#print(soup)
	list = []
	for item in soup.find_all(class_="odd"):
		list.append(item.text)
	for item in soup.find_all(class_="even"):
		list.append(item.text)
	dates = []
	revenues = []
	for item in list:
		removeNA = False
		date = item.split("$")[0]
		#print(date)
		try:
			revenue = item.split("$")[1]
		except:
			removeNA = True
		if(removeNA == False):
			dates.append(date)
			revenues.append(revenue)

	stacked = pd.DataFrame(np.column_stack([dates, revenues]), columns=['Date', 'Revenue'])
	stacked['Date'] =pd.to_datetime(stacked.Date)
	dateRevQuarterly = stacked.sort_values(by='Date', ascending=False)
	return dateRevQuarterly

#for item in soup.find_all(class_="ui-tabs-anchor"):
#	print(item.text)
#for item in soup.find_all(class_="sorting"):
#    print(item.text)
#for item in soup.find_all(class_="sorting_desc"):
#    print(item.text)



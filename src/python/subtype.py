import requests
import urllib
import json
import financials
import cik

def getSubType(cik, adsh):
	url = "https://www.sec.gov/Archives/edgar/data/" + cik + "/" + str(adsh).replace("-", "") + "/" + str(adsh) + "-index-headers.html"
	#print(url)
	resp = requests.get(url)
	data = resp.text
	index = data.find("CONFORMED SUBMISSION TYPE")
	#print(index)
	type = data[1187:1191]
	return type

'''
ticker = 'MSFT'
year = '2018'
quarter = '2'
data = financials.getReport(cik.tickerLookup(ticker), year, quarter)
print(cik.tickerLookup(ticker))
adshlist = data['adsh']
print(data)


print(adshlist)
for adsh in adshlist:
	print(getSubType(cik.tickerLookup('MSFT', asdh)))
'''
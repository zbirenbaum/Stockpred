import requests
import urllib
import json

def getSubType(cik, adsh):
	url = "https://www.sec.gov/Archives/edgar/data/" + cik + "/" + str(adsh).replace("-", "") + "/" + str(adsh) + "-index-headers.html"
	#print(url)
	resp = requests.get(url)
	data = resp.text
	index = data.find("CONFORMED SUBMISSION TYPE")
	#print(index)
	type = data[1187:1191]
	return type

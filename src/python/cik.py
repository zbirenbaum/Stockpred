import csv


def tickerLookup(ticker):
	with open('cik_ticker.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter='|')
		for row in reader:
			if(row['Ticker'] == ticker):
				return row['CIK']

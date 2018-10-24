import json

dataFile = open("dataFile.json").read()

test = json.loads(dataFile)
print(test['AAPL']['PropertyPlantAndEquipmentGross']['1']['value'])
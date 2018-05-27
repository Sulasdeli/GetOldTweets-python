import sys
import re
import codecs
import string
import requests
import time
import logging
from datetime import datetime
import os
import csv
import json

fields = []
rows = []

file = open(sys.argv[1])
reader = csv.reader(file, delimiter=';')
def sentimentAnalysis(tweetText):
    key = "YOUR_KEY"
	r = requests.post("https://language.googleapis.com/v1/documents:analyzeSentiment?fields=documentSentiment&key="+key,json.dumps( {
'document':{'type': "PLAIN_TEXT", 'content': tweetText}}))
	return (json.loads(r.text))

# extracting field names through first row
fields = reader.next()

# extracting each data row one by one
for row in reader:
    rows.append(row)

fields.append("magnitude_google")
fields.append("score_google")

for ro in rows:
    result = sentimentAnalysis(ro[7])['documentSentiment']
    ro.append(str(result['magnitude']))
    ro.append(str(result['score']))

outputFileName = "output_got.csv"
outputFile = codecs.open(outputFileName, "w+", "utf-8")

outputFile.write(";".join(fields))




for t in rows:
    outputFile.write("\n"+";".join(t))

outputFile.flush()



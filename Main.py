# _*_ coding=utf-8 _*_

import sys,getopt,datetime,codecs
import re
import random as rn
from string import ascii_letters, punctuation
import string
import requests
import json

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():

	def printTweet(t):
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)
		print("Date: %s\n" % t.date)
		print("Date: %s\n" % t.id)



	tweets=[]
	# Get tweets by query search
	for y in range(2017,2019):
		interval = range(0)
		month = ""
		if y == 2017:
			interval = range(7,32)
			month= "12"
		elif y == 2018:
			interval = range(1,8)
			month = "1"
		for i in interval:
			prefix=""
			if i<10:
				prefix ="0"
			else:
				prefix = ""
			if y==2017 and i ==31:
				tweetCriteria = got.manager.TweetCriteria().setQuerySearch('XRP ripple').setSince("2017-12-31").setUntil("2018-01-01").setMaxTweets(100)
				tweets.append(got.manager.TweetManager.getTweets(tweetCriteria))
			else:
				tweetCriteria = got.manager.TweetCriteria().setQuerySearch('XRP ripple').setSince(str(y)+"-"+month+"-"+prefix+str(i)).setUntil(str(y)+"-"+month+"-"+prefix+str(i+1)).setMaxTweets(100)
				tweets.append(got.manager.TweetManager.getTweets(tweetCriteria))
			print("extracting 100 tweets from:"+str(y)+"-"+month+"-"+prefix+str(i))
	outputFileName = "output_got.csv"
	outputFile = codecs.open(outputFileName, "w+", "utf-8")

	outputFile.write('date;text;id;polarity;permalink')



	for tw in tweets:
		counter = 0;
		output = [tweet for tweet in tw  if isEnglish(tweet.text)]
		for t in output:
			#From 100 tweets per day, select 5 randomly
			choice = rn.randint(0,10)
			if choice <5 and counter < 5 and re.search(r'btc|bitcoin|ethereum|eth',t.text.lower()) is None:
				counter+=1
				res =  sentimentAnalysis(t.text,t.id)
				outputFile.write(('\n%s;"%s";"%s";"%d";"%s"' % (t.date.strftime("%Y-%m-%d"), t.text,t.id,res,t.permalink)))
	outputFile.flush()


def isEnglish(s):
    return all(ord(c) < 128 for c in s)


def sentimentAnalysis(tweetText,tweetId):
	r = requests.post("http://www.sentiment140.com/api/bulkClassifyJson",json.dumps( {
'data':[{'text': tweetText[:30], 'id': tweetId}]}))
	return (json.loads(r.text)["data"][0]["polarity"])

if __name__ == '__main__':
	main()


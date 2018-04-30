import sys,getopt,datetime,codecs
import re
import random as rn
from string import ascii_letters, punctuation
import requests

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
			print(str(y)+"-"+month+"-"+prefix+str(i))
	
	#tweetCriteria2 = got.manager.TweetCriteria().setQuerySearch('XRP').setSince("2017-12-08").setUntil("2017-12-09").setMaxTweets(2)
	#tweets.append(got.manager.TweetManager.getTweets(tweetCriteria2))

	#for tweet in tweets:
	#	for tw in tweet:	
	#		printTweet(tw)
	outputFileName = "output_got.csv"
	outputFile = codecs.open(outputFileName, "w+", "utf-8")

	outputFile.write('date;retweets;text;hashtags;id;polarity;permalink')




	allowed = set(ascii_letters)
	for tw in tweets:
		counter = 0;
		output = [tweet for tweet in tw if any(letter in allowed for letter in tweet.text[:2])]
		for t in output:
			printTweet(t)
			#From 100 tweets per day, select 5 randomly
			choice = rn.randint(0,10)
			print(choice)
			if choice < 5 and counter < 5 and re.search(r'btc|bitcoin|ethereum|eth',t.text.lower()) is None:
				counter+=1
				outputFile.write(('\n%s;%d;"%s";"%s";"%s";"%s"' % (t.date.strftime("%Y-%m-%d"), t.retweets, t.text, t.hashtags,t.id,t.permalink)))
	outputFile.flush()
	print('More %d saved on file...\n' % len(tweets)*2)


def sentimentAnalysis():

	r = requests.post("http://www.sentiment140.com/api/bulkClassifyJson", {
'data': [{'text': "i. invest also. i don't understand wich time xrp up", 'id': 940007675131191000}]})
	print(r.status_code, r.reason)
	print(r.text[:300] + '...')

if __name__ == '__main__':
	main()


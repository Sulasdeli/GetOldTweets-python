import sys,getopt,datetime,codecs
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
			asd=""
 
			if i<10:
				asd ="0"
			else:
				asd = ""
			if y==2017 and i ==31:
				print("ERIONI FROCIO")
				tweetCriteria = got.manager.TweetCriteria().setQuerySearch('XRP').setSince("2017-12-31").setUntil("2018-01-01").setMaxTweets(2)
				tweets.append(got.manager.TweetManager.getTweets(tweetCriteria))
			else:
				tweetCriteria = got.manager.TweetCriteria().setQuerySearch('XRP').setSince(str(y)+"-"+month+"-"+asd+str(i)).setUntil(str(y)+"-"+month+"-"+asd+str(i+1)).setMaxTweets(2)
				tweets.append(got.manager.TweetManager.getTweets(tweetCriteria))
	
	#tweetCriteria2 = got.manager.TweetCriteria().setQuerySearch('XRP').setSince("2017-12-08").setUntil("2017-12-09").setMaxTweets(2)
	#tweets.append(got.manager.TweetManager.getTweets(tweetCriteria2))

	#for tweet in tweets:
	#	for tw in tweet:	
	#		printTweet(tw)
	outputFileName = "output_got.csv"
	outputFile = codecs.open(outputFileName, "w+", "utf-8")

	outputFile.write('date;retweets;text;hashtags')




	for tw in tweets:
		for t in tw:
			outputFile.write(('\n%s;%d;"%s";"%s"' % (t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.text, t.hashtags)))
	outputFile.flush()
	print('More %d saved on file...\n' % len(tweets)*2)


if __name__ == '__main__':
	main()

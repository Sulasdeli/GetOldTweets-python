import sys
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
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('XRP').setSince("2017-12-07").setUntil("2017-12-08").setMaxTweets(2)
	tweets.append(got.manager.TweetManager.getTweets(tweetCriteria))
	
	tweetCriteria2 = got.manager.TweetCriteria().setQuerySearch('XRP').setSince("2017-12-08").setUntil("2017-12-09").setMaxTweets(2)
	tweets.append(got.manager.TweetManager.getTweets(tweetCriteria2))

	for tweet in tweets:
		for tw in tweet:	
			printTweet(tw)


if __name__ == '__main__':
	main()

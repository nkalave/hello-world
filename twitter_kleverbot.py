# YouTube - url https://www.youtube.com/watch?v=o_OZdbCzHUA

import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'c7bkLgTqUQaUYgpNNKW6ChVCF'
consumer_secret= 'Fu0DzkfT1vbTMSHLvo5LwdB9hqMU1fdcEt5hGwvd4YsldHMQju'

access_token='817520080187584512-zy5JFTkofavn4Uq5VcrNUAO8gfyLlHo'
access_token_secret='lFecSzrIkGxivIG9McLYNn3U6DpJa83R3tScsCYdUq4Zl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
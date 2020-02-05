import sys, tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt


class Tweets():
    def __init__(self):
        
        self.tweet = "tweet"
        self.sentiment = 0
    
        #API keys
        API_key = "r0Gozz2N4hXymBYBaDSUXSyJX"
        API_secret_key = "pojIVOYhXWmsOUrBtj2JnNxSbQdKcZaf7mESM8D5VlMhbD9Xw8"
        access_token = "1219994617485066241-xlZ1AbuncHXqCXMY9BSavZHsayiNRo"
        access_token_secret = "5nozCn9hiXcWUyB7iE9AwiP1G5UOQsg2elnu6IWMJMnZI"

        #Connect to API
        auth = tweepy.OAuthHandler(consumer_key=API_key, consumer_secret=API_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


    def newTweet(self, searchTerm, username):
        #tweet = tweepy.Cursor(self.api.search, q=searchTerm, lang="English").items(1)

        tweets = self.api.user_timeline(screen_name = username, count = 200, truncated=False)
        
        for tweet in tweets:
            if searchTerm.lower() in tweet.text.lower():
                break

        
        tweetID = tweet.id
        
        tweet = self.api.get_status(tweetID, tweet_mode='extended')
        
 
        self.tweet = tweet.full_text
        
        sentiment = TextBlob(tweet.full_text)
    
        self.sentiment = sentiment.sentiment.polarity



    

    
    
    
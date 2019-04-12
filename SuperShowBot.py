from credentials import *
import tweepy
import QuoteMod

#Setting up OAuth and then integrating that with the API
authority = tweepy.OAuthHandler(consumer_key, consumer_secret)
authority.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = QuoteMod.GimmeQuote()
api.update_status(tweet)

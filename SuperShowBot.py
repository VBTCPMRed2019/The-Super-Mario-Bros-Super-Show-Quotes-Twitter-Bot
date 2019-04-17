from credentials import *
import tweepy
import QuoteMod
from time import sleep as wait
import os
import datetime

# This is the part where information, from an external module, is entered to allow the bot to be used
authority = tweepy.OAuthHandler(consumer_key, consumer_secret) 
authority.set_access_token(access_token, access_token_secret)
api = tweepy.API(authority, wait_on_rate_limit = True)

# Perpetual loop where it waits for certain times to send a tweet/update its status
while True:
    time = datetime.datetime.now()
    if time.hour == 11 and time.minute == 59: # 11:59 the bot's text file is cleared so it can reuse quotes it used the pervious day. 
        os.remove('UsedQuotes.txt')
        File = open("UsedQuotes.txt", "w+")
    if (time.hour == 24 or time.hour == 4 or time.hour == 8 or time.hour == 12 or time.hour == 16 or time.hour == 20) and (time.minute == 0 and time.second < 59): 
        message = QuoteMod.GimmeQuote()
        print(message)
        api.update_status(message)
        wait(80)
        
# A future idea where the bot will respond when it is @'d
    #tweets = api.search("@SmbssQ")
    #if tweets == True:
        #screen_name = s.user.screen_name
        #message = ("@",screen_name, QuoteMod.GimmeQuote())
        #api.update_status(message)
        #tweets = ''
        #wait(60)

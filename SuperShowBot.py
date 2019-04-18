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

def ClearFile(File): #Erases the content of the File, is only called when there are more than 230 quotes in "UsedQuotes.txt"
    File.seek(0)
    File.truncate()
    
File = open("UsedQuotes.txt", "w+") #Opens "UsedQuotes.txt" or creates it if it does not exist

# Perpetual loop where it waits for certain times to send a tweet/update its status
while True:
    time = datetime.datetime.now()
    line_count = len(open("UsedQuotes.txt").readlines())
    if (time.hour == 24 or time.hour == 4 or time.hour == 8 or time.hour == 12 or time.hour == 16 or time.hour == 20) and (time.minute == 0 and time.second < 59): 
        message = QuoteMod.GimmeQuote()
        print(message)
        api.update_status(message)
        if line_count > 230: 
            ClearFile(File)
        wait(80)
        
# A future idea where the bot will respond when it is @'d
    #tweets = api.search("@SmbssQ")
    #if tweets == True:
        #screen_name = s.user.screen_name
        #message = ("@",screen_name, QuoteMod.GimmeQuote())
        #api.update_status(message)
        #tweets = ''
        #wait(60)

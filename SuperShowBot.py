from credentials import *
import tweepy
import QuoteMod
import time
import datetime

localtime = time.asctime(time.localtime(time.time())) #Prints when the program was initially ran
print('Program started on:', localtime)

# This is the part where information, from an external module, is entered to allow the bot to be used
authority = tweepy.OAuthHandler(consumer_key, consumer_secret) 
authority.set_access_token(access_token, access_token_secret)
api = tweepy.API(authority, wait_on_rate_limit = True)

def ClearFile(File): #Erases the content of the File, is only called when there are more than 230 quotes in "UsedQuotes.txt"
    File.seek(0)
    File.truncate()
    
try: #Opens the file if it exist, if the file does not exist it creates it.
    File = open("UsedQuotes.txt", "r")
except FileNotFoundError:
    File = open("UsedQuotes.txt", "w+")
    
# Perpetual loop where it waits for certain times to send a tweet/update its status
while True:
    time = datetime.datetime.now()
    line_count = len(open("UsedQuotes.txt").readlines())
    if (time.hour == 24 or time.hour == 4 or time.hour == 8 or time.hour == 12 or time.hour == 16 or time.hour == 20) and (time.minute == 0 and time.second < 59): 
        message = QuoteMod.GimmeQuote()
        print(message)
        api.update_status(message)
    if line_count > 230: 
        File = open("UsedQuotes.txt", "w+")
    time.sleep(80)
        
File.close()

'''
tweets = api.search("@SmbssQ") #Searches for the keywords "@SmbssQ", at the moment it does not work.
if tweets == True:
    tweet_list = ['@smbssq', '@SMBSSQ', '@SmbssQ']
    for s in tweets:
        for i in tweet_list:
            if i == s.text:
                screen_name = s.user.screen_name
                message = "@{0}\n{1}".format(screen_name, QuoteMod.GimmeQuote())
                print(message)
                api.update_status(message, s.id)   
  '''


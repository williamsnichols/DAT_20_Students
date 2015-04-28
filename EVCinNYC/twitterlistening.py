import requests     # how python goes onto the internet!
import tweepy       # python wrapper for twitter api
import json         # javascript object notation
import time         # timey wimey stuff
import re           # regex

#first four keys are from the Twitter account, the last from MashApe
#these are specific to my accounts @FreshPopSmash and EVCinNYC
api_key = "aSX83jGxUoymHL8KfX0hOp2zn"
api_secret = "PPizvnwskCYdaGv7yG17UALSQiiSjTccwlFpdJR8Q1u6MtbTHx"
access_token = "2366325853-T94YmBYVxOMNmSEP1dZ95iTDiamkbNAj5oJEzHw"
access_secret = "RnHVp0ZSFcGun4IJBZAoBNgqJStYIp7R0kb02C8FxWYst"
mashape_key = "7po6lyWFk6mshDBIZltKH10NC5CAp1UMzPajsnvRe1fehSZEBl"

#from MashApe we added the japerk sentiment API so we could add this below
#have to define it here first
def get_sentiment(phrase):
    response = requests.post("https://japerk-text-processing.p.mashape.com/sentiment/",
    headers={
        "X-Mashape-Key": mashape_key,
        "Content-Type": "application/x-www-form-urlencoded"
        },
    data={
        "language": "english",
        "text": phrase
        }
    )
    return json.loads(response.text)


def getTweetsOnTag(tag):
	
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth) # returns a tweepy authorization handler object
    for tweet in api.search(q=tag):
        # other arguments exist, CHECK DOCUMENTATION
        # print tweet # is a BIG dictionary!!
        print tweet.created_at, tweet.text
        
# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        time_ =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(decoded['timestamp_ms']) / 1000))
        handle = decoded['user']['screen_name']
        tweet_text = decoded['text'].encode('ascii', 'ignore')
        num_followers = int(decoded['user']['followers_count'])

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s at %s: %s with %d followers' % (handle, time_, tweet_text, num_followers)
        print 'sentiment: '+get_sentiment(tweet_text)['label']
        print ''
        return True
    def on_error(self, status):
        print status

def begin_live_feed(tags_to_follow):
    print "beginning live feed...."
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=tags_to_follow)

# begin_live_feed(['@ga', '@ga_ny', '@ga_dc'])

term = raw_input(" term to search: ")
print "begin_live_feed([\"%s\"])" %(term)
begin_live_feed([term]) 
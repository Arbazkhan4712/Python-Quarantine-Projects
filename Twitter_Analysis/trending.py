import tweepy
import json
from twitter_credentials import CONSUMER_KEY,ACCESS_TOKEN_SECRET,ACCESS_TOKEN,CONSUMER_SECRET

def authentication():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth
    except:
        print('Error Authentication')

def trending_topics():
    valid_token=authentication()
    api = tweepy.API(valid_token)
    trends = api.trends_place(1)

    data = trends[0]

    data_keys=data.keys()


    trends = data['trends']
    names = [i['name'] for i in trends]
    tweet_vol = [i['tweet_volume'] for i in trends]
    location = data['locations']
    started_at=data['created_at']

    return (names,tweet_vol,location,started_at)


#print(trending_topics())
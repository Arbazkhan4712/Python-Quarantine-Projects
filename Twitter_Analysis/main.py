from tweepy_streamer import start
from trending import trending_topics


def trending_fetch():
    (names,tweet_vol,location,started_at)=trending_topics()
    print('Top 10 trending things around the world : '+str(started_at)+':\n')
    for i in range(0,10):
        print(names[i],"   ",str(tweet_vol[i]))
    
    
    

def feed_fetch():
    ip_words=(input('Please enter the keywords to search (for 1 or more keywords use ","): '))
    print(start(ip_words))



feed_fetch()
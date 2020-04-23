import sqlite3
import json
from tqdm import tqdm
from text_analysis import senti_score,sentiment_analyzer

data=[]

with open('tweets.txt','r') as f:
    raw_data=f.readlines()

for i in raw_data:
    if len(i)>1:
        data.append(i)

##################################################################################################--DATABASE INSERT--################################################################################################

def data_injester(id,created_at,usr_name,dp_name,location,verified_acc,protected_tweet,follow_cnt,pro_pic,hash_tags,tweet_txt,descr,source_url,likes,status_cnt,retweeted,full_url):
    try:
        conn = sqlite3.connect('data.sql')
        cur = conn.cursor()
        cmd='insert into tweet_data (id,created_at,usr_name,dp_name,location,verified_acc,protected_tweet,follow_cnt,pro_pic,hash_tags,tweet_txt,descr,source_url,likes,status_cnt,retweeted,full_url) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        cur.execute(cmd,(id,created_at,usr_name,dp_name,location,verified_acc,protected_tweet,follow_cnt,pro_pic,hash_tags,tweet_txt,descr,source_url,likes,status_cnt,retweeted,full_url))
        conn.commit()
    except:
        print('Failed Data load')
    finally:
        conn.commit()
        conn.close()

def score_view_insert(id,usr_name,tweet_txt,descr,pos_words,neu_words,neg_words,score):            #Insert data into the tweets_analysis after score generation
    # try:
    conn = sqlite3.connect('data.sql')
    cur = conn.cursor()
    cmd='insert into tweet_analysis (id,usr_name,tweets,descr,Positive_words,Neutral_words,Negative_words,SID_Score) values (?,?,?,?,?,?,?,?)'
    cur.execute(cmd,(id,usr_name,tweet_txt,descr,pos_words,neu_words,neg_words,score))
    conn.commit()
    # except:
    #     print('Failed Data load')
    # finally:
    #     conn.commit()
    conn.close()

def score_view():
    try:
        conn = sqlite3.connect('data.sql')
        cur = conn.cursor()
        cmd='select id,usr_name,tweet_txt,descr from tweet_data'
        cur.execute(cmd)
        op=cur.fetchall()
        return op
    except:
        print('Failed Data load')
    finally:
        conn.close()

###################################################################################################-- SCORE GENERATOR--################################################################################################

def score_gen():
    c=0
    op=score_view()
    for i in tqdm(op):
        id=i[0]
        usr_name=i[1]
        if i[2] and i[3] is not None:
            tweet=i[2]
            descr=i[3]
            score=senti_score(descr)
        else:
            tweet='NULL'
            descr='NULL'
            score=0
        c+=1
        pos_wrd,neu_wrd,neg_wrd=sentiment_analyzer(descr)
        score_view_insert(id,usr_name,tweet,descr,pos_wrd,neu_wrd,neg_wrd,score)
    print('Total Insertion: '+str(c))

score_gen()

###############################################################################################-- DATA EXTRACTOR --###################################################################################################

def data_loader():
    for i in tqdm(data):
        id=json.loads(i)['id']
        created_at=json.loads(i)['created_at']
        usr_name=json.loads(i)['user']['name']
        dp_name=json.loads(i)['user']['screen_name']
        location=json.loads(i)['user']['location']
        verified_acc=json.loads(i)['user']['verified']
        protected_tweet=json.loads(i)['user']['protected']
        follow_cnt=json.loads(i)['user']['followers_count']
        friends_cnt=json.loads(i)['user']['friends_count']
        pro_pic=json.loads(i)['user']['profile_image_url']
        tag=json.loads(i)['entities']['hashtags'] 
        hash_tags=",".join([i["text"] for i in tag])
        tweet_txt=json.loads(i)['text']
        descr=json.loads(i)['user']['description']
        source_url=json.loads(i)['source']
        likes=json.loads(i)['user']['favourites_count']
        status_cnt=json.loads(i)['user']['statuses_count']
        retweeted=json.loads(i)['retweeted']
        url=json.loads(i)['entities']['urls']
        full_url = "".join([i["expanded_url"] for i in url])


        data_injester(id,created_at,usr_name,dp_name,location,verified_acc,protected_tweet,follow_cnt,pro_pic,hash_tags,tweet_txt,descr,source_url,likes,status_cnt,retweeted,full_url)
    
    data_count=len(data)
    print('Total Data load: ',data_count)
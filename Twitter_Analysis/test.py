import sqlite3
import json
from tqdm import tqdm
from text_analysis import senti_score,sentiment_analyzer


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

######################################################################################################################################################################################################################

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
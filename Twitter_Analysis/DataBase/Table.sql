drop table tweet_data ;
drop table tweet_analysis ;


CREATE TABLE tweet_data (id text,
created_at timestamp,
usr_name text,
dp_name text,
location text,
verified_acc text,
protected_tweet text,
follow_cnt  integer,
pro_pic text,
hash_tags text,
tweet_txt text,
descr text,
source_url text,
likes integer ,
status_cnt integer,
retweeted integer,
full_url text);

CREATE TABLE tweet_analysis(
id text,
usr_name text,
tweets text,
descr text,
Positive_words text,
Neutral_words text,
Negative_words text,
SID_Score integer);


delete from tweet_data;
DELETE  from tweet_analysis;

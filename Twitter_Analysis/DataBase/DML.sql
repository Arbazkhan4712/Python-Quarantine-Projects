
select * from tweet_data td ;

select COUNT(*) from tweet_data td ;   --1865   --23354


select id,usr_name,location,follow_cnt,descr,tweet_txt ,likes,status_cnt from tweet_data td where location like '%india%';


select COUNT(*) from tweet_data td where location like '%india%';  --233

select id,usr_name,location,follow_cnt,likes,status_cnt,polarity_score,subjectivity_score from tweet_data td where location  like '%india' order by follow_cnt DESC ;

select count(*) from tweet_data td where location is null;  --599



select * from tweet_data td where id='1251356833639350278'


------------------------------------------------------------------------------------------------------------

SELECT COUNT(*) from tweet_analysis ta ;     --23368

select * from tweet_analysis ta ;


select Positive_words from tweet_analysis ta where Positive_words NOTNULL ;



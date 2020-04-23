from rake_nltk import Rake
import nltk,re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

data_ip='Innovative Incentives & Rewards, a full service corporate relationship marketing agency specializing in Customer #Loyalty Programs & #Reward Management in India'.split(' ')


def sentiment_analyzer(test_subset):      #Analyses the state of the words
    sid = SentimentIntensityAnalyzer()
    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[]

    for word in test_subset:
        if (sid.polarity_scores(word)['compound']) >= 0.5:
            pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.5:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)         

    print('Positive :',pos_word_list)        
    print('Neutral :',neu_word_list)    
    print('Negative :',neg_word_list) 


op=sentiment_analyzer(data_ip)
print(op)
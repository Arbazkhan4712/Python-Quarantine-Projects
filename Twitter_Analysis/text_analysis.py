from rake_nltk import Rake
import nltk,re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

data_ip='Innovative Incentives & Rewards, a full service corporate relationship marketing agency specializing in Customer #Loyalty Programs & #Reward Management in India'


def rank_words(data_ip):
    r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
    r.extract_keywords_from_text(data_ip)
    return r.get_ranked_phrases()

def sentiment_analyzer(test_subset):      #Analyses the state of the words
    sid = SentimentIntensityAnalyzer()

    test_subset=rank_words(test_subset)
    
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
    
    pos_word_list=' '.join(pos_word_list)
    neu_word_list=' '.join(neu_word_list)
    neg_word_list=' '.join(neg_word_list)

#    print('Positive :',pos_word_list)        
#    print('Neutral :',neu_word_list)    
#    print('Negative :',neg_word_list) 
    return pos_word_list,neu_word_list,neg_word_list


def senti_score(test_subset):#Analyses the state of the words
    sid = SentimentIntensityAnalyzer()

    senti_score=sid.polarity_scores(test_subset)['compound']
    return senti_score


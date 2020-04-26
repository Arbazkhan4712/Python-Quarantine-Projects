import pandas as pd
import numpy as np
bots = pd.read_csv('bots_data.csv',encoding='latin-1')
nonbots = pd.read_csv('nonbots_data.csv',encoding='latin-1')
#bots[bots.listedcount>10000]
condition = (bots.screen_name.str.contains("bot", case=False)==True)|(bots.description.str.contains("bot", case=False)==True)|(bots.location.isnull())|(bots.verified==False)

bots['screen_name_binary'] = (bots.screen_name.str.contains("bot", case=False)==True)
bots['description_binary'] = (bots.description.str.contains("bot", case=False)==True)
#bots['location_binary'] = (bots.location.isnull())
bots['verified_binary'] = (bots.verified==False)
print("Bots shape: {0}".format(bots.shape))

#Creating NonBots identifying condition
condition = (nonbots.screen_name.str.contains("bot", case=False)==False)| (nonbots.description.str.contains("bot", case=False)==False) |(nonbots.location.isnull()==False)|(nonbots.verified==True)

nonbots['screen_name_binary'] = (nonbots.screen_name.str.contains("bot", case=False)==False)
nonbots['description_binary'] = (nonbots.description.str.contains("bot", case=False)==False)
#nonbots['location_binary'] = (nonbots.location.isnull()==False)
nonbots['verified_binary'] = (nonbots.verified==True)
print("Nonbots shape: {0}".format(nonbots.shape))

#Joining Bots and NonBots dataframes
df = pd.concat([bots, nonbots])
print("DataFrames created...")

#Splitting data randombly into train_df and test_df
from sklearn.model_selection import train_test_split
train_df, test_df = train_test_split(df, test_size=0.2)
print("Randomly splitting the dataset into training and test, and training classifiers...\n")

#Using Decision Tree Classifier
#from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB(alpha=1, fit_prior=True)
#clf = DecisionTreeClassifier(criterion='entropy')

#80%
X_train = train_df[['screen_name_binary', 'description_binary',  'verified_binary']] #train_data
y_train = train_df['bot'] #train_target

#20%
X_test = test_df[['screen_name_binary', 'description_binary',  'verified_binary']] #test_Data

#Training on decision tree classifier
model = clf.fit(X_train, y_train)

from sklearn.externals import joblib
joblib.dump(model,'model.pkl')
joblib.dump(X_test,'X_test.pkl')

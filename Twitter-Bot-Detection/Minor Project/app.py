from flask import Flask,request,jsonify,render_template,url_for,redirect
from sklearn.externals import joblib
import pandas as pd

import os
import sys
scriptpath = "D:\\Minor Project"
sys.path.append(os.path.abspath(scriptpath))
import  twitterbot
app=Flask(__name__)
def ValuePredictor(to_predict): 
    #to_predict = np.array(to_predict_list).reshape(1,3) 
    model=joblib.load('model.pkl')
    result = model.predict(to_predict) 
    return result
@app.route('/')
def home():
    return render_template('index.html')
'''@app.route('/predict/<prediction>')
def predict(prediction):
    return render_template("predict.html",prediction=prediction)'''
@app.route('/predict',methods=['POST'])
def predict():
	#df = request.form.to_dict(flat=False) 
	#to_predict_list = list(to_predict_list.values()) 
    #to_predict_list = list(map(int,to_predict_list))
     
	#data=[]
	data=["request.form.get('screen_name')","df['description']=request.form.get('description')","df['verified']=request.form.get('verified')"]
	s1=[data]
	df = pd.DataFrame(s1, columns=['screen_name', 'description','verified'])
	x=request.form.get('verified')
	x1=request.form.get('screen_name')
	x2=request.form.get('description')
	'''df['id']=request.form["id"]
	print(df['id'])

	#df['screen_name']=request.form['screen_name']
	#df['description']=request.form['description']
	df['followers_count']=request.form['followers_count']
	df['friends_count']=request.form['friends_count']
	df['listed_count']=request.form['listed_count']
	#df['verified']=request.form['verified']
	#df['status']=request.form['status']
	#df['name']=request.form['name']
	
	#df['location_binary'] = (df.location.isnull())'''
	if "bot" in x1:
		df['screen_name_binary'] = True
	else:
		df['screen_name_binary'] = False

	if "bot" in x2:
		df['description_binary'] = True
	else:
		df['description_binary'] = False
	if x=='0':
		df['verified_binary']=False
	else:
		df['verified_binary']=True
	df = df[['screen_name_binary', 'description_binary', 'verified_binary']]
	result = ValuePredictor(df)
	if result==0:
		prediction='It is a BOT'
	else:
		prediction="It is a HUMAN"
	'''
    if df['verified']>1:
		df['verified_binary'] = False 
		prediction='It is a BOT'
	else:
		df['verified_binary'] = True
		prediction="It is a NONBOT"
	df = df[['screen_name_binary', 'description_binary', 'verified_binary']]
	
	
	
	df['screen_name_binary'] = 0
	df['description_binary'] = 1
	df['verified_binary'] = 1
	df = df[['screen_name_binary', 'description_binary', 'verified_binary']]
	if int(result)== 1:
        prediction='NonBot'
    else:
        prediction='Income less that 50K'''           
    #return render_template("result.html", prediction = prediction)
 #model=joblib.load('model.pkl')
	#predict=model.predict(X_test)
	#predicted=twitterbot.twitter_bot.bot_prediction_algorithm(df)
	#return redirect(url_for('/predict',prediction=result))
	return render_template("index.html", prediction = prediction)

if __name__ =='__main__':
    app.run(port=3000,debug=True)
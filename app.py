from flask import Flask, render_template, request,redirect,url_for
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('decision_tree_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route('/result',methods=['POST'])
def result():
    return render_template('result.html')


@app.route("/predict", methods=['POST'])
def predict():
	temp_array = list()
	if request.method=='POST':


	  # Batting Team
	  batting_team=request.form['batting_team']
	  if batting_team == 'Chennai Super Kings':
	    temp_array = temp_array + [1,0,0,0,0,0,0,0]
	  elif batting_team == 'Delhi Daredevils':
	    temp_array = temp_array + [0,1,0,0,0,0,0,0]
	  elif batting_team == 'Kings XI Punjab':
	    temp_array = temp_array + [0,0,1,0,0,0,0,0]
	  elif batting_team == 'Kolkata Knight Riders':
	    temp_array = temp_array + [0,0,0,1,0,0,0,0]
	  elif batting_team == 'Mumbai Indians':
	    temp_array = temp_array + [0,0,0,0,1,0,0,0]
	  elif batting_team == 'Rajasthan Royals':
	    temp_array = temp_array + [0,0,0,0,0,1,0,0]
	  elif batting_team == 'Royal Challengers Bangalore':
	    temp_array = temp_array + [0,0,0,0,0,0,1,0]
	  elif batting_team == 'Sunrisers Hyderabad':
	    temp_array = temp_array + [0,0,0,0,0,0,0,1]

	  # Bowling Team
	  bowling_team=request.form['bowling_team']
	  if bowling_team == 'Chennai Super Kings':
	    temp_array = temp_array + [1,0,0,0,0,0,0,0]
	  elif bowling_team == 'Delhi Daredevils':
	    temp_array = temp_array + [0,1,0,0,0,0,0,0]
	  elif bowling_team == 'Kings XI Punjab':
	    temp_array = temp_array + [0,0,1,0,0,0,0,0]
	  elif bowling_team == 'Kolkata Knight Riders':
	    temp_array = temp_array + [0,0,0,1,0,0,0,0]
	  elif bowling_team == 'Mumbai Indians':
	    temp_array = temp_array + [0,0,0,0,1,0,0,0]
	  elif bowling_team == 'Rajasthan Royals':
	    temp_array = temp_array + [0,0,0,0,0,1,0,0]
	  elif bowling_team == 'Royal Challengers Bangalore':
	    temp_array = temp_array + [0,0,0,0,0,0,1,0]
	  elif bowling_team == 'Sunrisers Hyderabad':
	    temp_array = temp_array + [0,0,0,0,0,0,0,1]

	  # Overs, Runs, Wickets, Runs_in_prev_5, Wickets_in_prev_5
	  overs=float(request.form['overs'])
	  runs=int(request.form['runs'])
	  wickets=int(request.form['wickets'])
	  runs_in_prev_5=int(request.form['runs_in_prev_5'])
	  wickets_in_prev_5=int(request.form['wickets_in_prev_5'])
	  temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

	  # Converting into numpy array
	  temp_array = np.array([temp_array])

	  # Prediction
	  final_score= int(model.predict(temp_array)[0])
	  return render_template('result.html',final_score=final_score)







if __name__=="__main__":
    app.run(debug=True)

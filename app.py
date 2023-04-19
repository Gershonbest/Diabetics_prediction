import pickle
from pydoc import render_doc 
from flask import Flask, request,app, jsonify, url_for, render_template
from os import path
import numpy as np
import pandas as pd
import json



app = Flask(__name__)


# we load the pickle file as the model
ML_model = pickle.load(open('Model/random_f2.pkl', 'rb'))


@app.route('/') # homepage
def home():
     return render_template('home.html')
    
    
# @app.route('/login', methods= ['GET', 'POST']) # login page
@app.route('/login') # login page
def login():
     username = request.form.get("username")
     password = request.form.get("password")
     
     return render_template('login.html')

@app.route('/signup', methods= ['GET', 'POST']) # login page
def signup():
     first_name = request.form.get("first_name")
     last_name = request.form.get("last_name")
     username = request.form.get("username")
     email = request.form.get("email")
     password = request.form.get("passwor")
     
     return render_template('signup.html')



@app.route('/index')
def index():
     return render_template('index.html')

@app.route('/predict')
def predict():
    data=[float(x) for x in request.form.values()]
    final_input = np.array(data).reshape((1, -1))
    print(final_input)
    output= ML_model.predict(final_input)[0]
    
    if output == 0:
         prediction = 'Congratulation you are diabetics free'
         
    elif output == 1:
         prediction = 'You are Diabetics type 2 positive'
         
    else:
         prediction = "you're prediabetics positive"
    return render_template('home2.html', prediction_text= prediction)
     # return render_template('predict.html')
     
@app.route('/predict_api', methods=['POST'])
def predict_api():
    # data=[float(x) for x in request.form.values()]
    data=request.json['data']
    print(data)
    new_data = np.array(list(data.values())).reshape(1,-1)
#     final_input = np.array(data).reshape((1, -1))
    final_input = np.array(new_data)
    print(final_input)
    output= ML_model.predict(final_input)
    
    if output[0] == 0.0:
         prediction = "Congratulation you are diabetics free"
         
    elif output[0] == 1.0:
         prediction = "You are Diabetics type 2 positive"
         
    else:
         prediction = "You are prediabetics positive"
         

#     return (prediction)
    return render_template('home2.html', prediction_text= prediction)
     # return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
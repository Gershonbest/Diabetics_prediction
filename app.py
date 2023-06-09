import pickle
from pydoc import render_doc 
from flask import Flask, request,app, jsonify, url_for, render_template
from os import path
import numpy as np
import pandas as pd
import json
from calculation import body_mass_index
from flask_mysqldb import MySQL
import pyrebase

config = {
  "apiKey": "AIzaSyDYj1iGWF4oEnnWgpFD0irW6Aa-d1vHLz0",
  "authDomain": "patient-log-dd421.firebaseapp.com",
  "projectId": "patient-log-dd421",
  "storageBucket": "patient-log-dd421.appspot.com",
  "messagingSenderId": "914441984103",
  "appId": "1:914441984103:web:04debe8be38122298adcc2",
  "measurementId": "G-SZHHW7CB6N"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'sql7.freemysqlhosting.net'
# app.config['MYSQL_USER'] = 'sql7613206'
# app.config['MYSQL_PASSWORD'] = '35J2rdLMU8'
# app.config['MYSQL_DB'] = 'sql7613206'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# mysql = MySQL(app)
# we load the pickle file as the model
ML_model = pickle.load(open('Model/random_f2.pkl', 'rb'))


@app.route('/', methods = ['GET', 'POST'] ) # homepage
def home():
    
     return render_template('home.html')
     
@app.route('/check_bmi', methods= ['POST','GET'])
def check_bmi():
     
    bmi_result = 0

    if request.method == 'POST':
          mass = request.form.get("mass")
          height = request.form.get("height")
          print(mass)
          bmi = body_mass_index(mass, height)
     
     
          bmi_result = bmi.bmi_kg_meter()
          
          # bmi_result= int(float(mass) / (float(height)*float(height)))
    else:
        pass
    if bmi_result != 0:
         
         if (bmi_result <18.5):
              message = "You are under weighted with your BMI: {:.2f}".format(bmi_result)
              return render_template('bmi_calc.html', bmi_results = message)
         
         elif ((bmi_result >= 18.5) & (bmi_result < 25)):
              message = "You have a healthy weight with your BMI: {:.2f}".format(bmi_result)
              return render_template('bmi_calc.html', bmi_results = message)
         
         elif ((bmi_result >= 25) & (bmi_result < 30)):
              message = "You are Over weighted with your BMI: {:.2f}".format(bmi_result)
              return render_template('bmi_calc.html', bmi_results = message)
         
         else:
              message= "You are on obesity stage with your BMI: {:.2f}".format(bmi_result)
              return render_template('bmi_calc.html', bmi_results = message)
    else:
          return render_template('bmi_calc.html')
    
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
     email = request.form.get("email")
     password1 = request.form.get("password1")
     password2 = request.form.get("password2")
     
     return render_template('signup.html')



@app.route('/index')
def index():
     return render_template('index3.html')

@app.route('/predict', methods= ['POST'])
def predict():
     
    bmi = request.form.get('bmi')
    data=[float(x) for x in request.form.values()]
    print(data)
    final_input = np.array(data).reshape((1, -1))
     
       
       
    print(final_input)
    output= ML_model.predict(final_input)
    
    if output[0] == 0.0:
         prediction = 'Congratulation you are diabetics free'
         
    elif output[0] == 1.0:
         prediction = 'You are Diabetics type 2 positive'
         
    else:
         prediction = "you're prediabetics positive"
    return render_template('index3.html', prediction_text= prediction)
     # return render_template('predict.html')
     
     
# @app.route('/log')
# def log():
#     cur = mysql.connection.cursor()
#     # cur.execute("SELECT * FROM health_record ORDER BY ID DESC")
#     cur.execute("SELECT id, patient_reg_no, BPM, SpO2, body_temp, time, date FROM health_record")
#     data = cur.fetchall()
#     # return str(data)
#     return render_template('log.html', data= data)

if __name__ == '__main__':
    app.run(debug=True)
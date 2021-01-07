# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
# Load the regression model
classifier = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    age = int(request.form['age'])
    job = int(request.form['job'])
    balance = int(request.form['balance'])
    days = int(request.form['days'])
    months = int(request.form['months'])
    duration = int(request.form['duration'])
    poutcome = int(request.form['poutcome'])
    pdays = int(request.form['pdays'])

    data = [[age, job, balance, days, months, duration, poutcome, pdays]]
    if (age==0 and job==0 and balance==0 and days==0 and months==0 and duration==0 and poutcome==0 and pdays==0):
        my_prediction = [0]
    else:
        my_prediction = classifier.predict(data)
        
        if my_prediction[0] == 0:
            return render_template('index.html', prediction_text='Response of the customer would be negative towards the campaign.')
        else:
            return render_template('index.html', prediction_text='Response of the customer would be positive towards the campaign.')



if __name__ == "__main__":
    app.run(debug=True)
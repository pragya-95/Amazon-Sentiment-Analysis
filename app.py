from copyreg import pickle
from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle
import bcrypt
import re
import json


vect = pickle.load(open("C:/Users/USER/Amazon/final_vectorizer.sav",'rb'))
model = pickle.load(open("C:/Users/USER/Amazon/final_model.sav",'rb'))

def cleanText(text):
    text = [t for t in text.split(' ') if t not in re.findall('@\w+|http[a-z:,/.0-9]+',text) and len(t) >2]
    text = ' '.join(text)
    text = ' '.join(re.findall('\w+',text))
    return text

app = Flask(__name__)


@app.route('/Predict/<rv>' ,methods=['POST','GET'])
def home(rv):
    data1= rv
    data1=cleanText(data1)
    data1=[data1]
    data2=vect.transform(data1)
    pred=model.predict(data2)
    data = {}
    data['pred'] = pred.tolist()[0]
    json_data = json.dumps(data)
    return json_data


@app.route('/',methods=['GET'])
def main():
	return render_template("frontend.html")

if __name__=='__main__':
    app.run(debug=True)
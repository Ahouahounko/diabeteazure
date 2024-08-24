from flask import Flask, request, render_template
import pickle
import numpy as np 
import pandas as pd 
from joblib import load


app = Flask(__name__)


# Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))



# regmodel = load('regmodel.joblib')
# scalar = load('scaling.joblib')



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods= ["POST"])
def prediction():
    data = [float(request.form[var]) for var in ['age', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']]
    data = np.array(data).reshape(1, -1)
    data = scalar.transform(data)
    prediction = regmodel.predict(data)[0]
    return render_template("home.html", prediction_text = "Expected diabete progression {:.2f}".format(prediction))


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)
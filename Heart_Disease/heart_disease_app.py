# -*- coding: utf-8 -*-

import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
try:
    model = pickle.load(open('/model.pkl', 'rb')) 
except:
    model = pickle.load(open('Heart_Disease\model.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    try:
        print("try")
        return render_template('Heart_Disease_Classifier.html')

    except:
        print("except")
        return render_template('Heart_Disease\Heart_Disease_Classifier.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('Heart_Disease_Classifier.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('Heart_Disease_Classifier.html', 
                               result = 'The patient is likely to have heart disease!')

if __name__ == '__main__':
#Run the application
    app.run()
    
    
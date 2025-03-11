
from flask import Flask, render_template,render_template_string, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

# load your pickle file and scalar 
with open('train3133.pkl', 'rb') as file:
    train3133 = pickle.load(file)
model=train3133["model"]
scalar=train3133["scalar"]
#This is the front page on continue press it open index.html
@app.route('/')
def front():
    return render_template('front.html')
#Here is a page for enter the data by user
@app.route('/index')
def index():
    return render_template('index.html')

#here enter data come and by process it generate output of prediction
@app.route('/predict', methods=['POST','GET'])
def predict():
    # Extract input values from form
    area= int(request.form['area'])
    bedrooms= int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])
    mainroad = int(request.form['mainroad'])
    guestroom= int(request.form['guestroom'])
    basement= int(request.form['basement'])
    hotwaterheating= int(request.form['hotwaterheating'])
    airconditioning= int(request.form['airconditioning'])
    parking= int(request.form['parking'])
    prefarea= int(request.form['prefarea'])
    furnishingstatus= float(request.form['furnishingstatus'])


    # Create input array for the model
    input_data = np.array([[area, bedrooms, bathrooms, stories,mainroad,guestroom, basement, hotwaterheating, airconditioning,parking, prefarea, furnishingstatus]])
    
    #that array is in 12 rows 1 column that convert into 1 row 12 columns
    test_array =input_data.reshape(1, 12)

    #Making the dataframe of the array
    res=pd.DataFrame(test_array,columns=[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
       'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
       'parking', 'prefarea', 'furnishingstatus']])
    
    #Transform the data
    x_scale=scalar.transform(res)

    x1=pd.DataFrame(x_scale,columns=[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
       'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
       'parking', 'prefarea', 'furnishingstatus']])
   
    
   
    #Make prediction
    prediction = model.predict(x1)

    #Return the result
    result = prediction[0]
    return render_template_string (f'''<html>
    <head><title>False alarm Detection Result</title></head>
    <body>
    <h1>{result}</h1><hr>
    # <h1>Result:</h1><hr>
    # <h3>Input Data:</h3><br>
    # <h3>Area:{area}</h3><br>
    # <h3>Furnishing Status:{furnishingstatus}</h3><br>
    # <h3>Prefarea:{prefarea}</h3><br>
    # <h3>Bathrooms:{bathrooms}</h3><br>
    # <h3>Bedrooms:{bedrooms}</h3><br>
    # <h3>Stories:{stories}</h3>
    # <hr>
    # <h1><b>Result</b></h1>
    # <h1>{result}</h1>
    # <br>
    # <h1><i>Thank You......</i></h1>
    # </body>
    # </html>''')

if __name__ == '__main__':
    app.run(debug=True,port=5002)
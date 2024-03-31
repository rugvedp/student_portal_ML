from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

model = pickle.load(open('model.pkl', 'rb'))

data = pd.read_csv("students1111.csv")
le_major = LabelEncoder()
le_domain = LabelEncoder()
le_projects = LabelEncoder()
data["Major"] = le_major.fit_transform(data["Major"])
data["Interested Domain"] = le_domain.fit_transform(data["Interested Domain"])
data["Projects"] = le_projects.fit_transform(data["Projects"])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    domain = request.form['domain']
    project = request.form["project"]
    python =  request.form["pythonRadio"]
    sql =  request.form["mysqlRadio"]
    java =  request.form["javaRadio"]

    eznums = {
      'Strong': 2,
      'Average': 1,
      'Weak': 0,
    }
    numericValuePY = eznums[python]
    numericValueSQL = eznums[sql]
    numericValueJAVA = eznums[java]
    encoded_domain = le_domain.transform([domain])
    encoded_projects = le_projects.transform([project])

    prediction = model.predict([[0,encoded_domain[0], encoded_projects[0], numericValuePY, numericValueSQL,numericValueJAVA]])   

    return render_template('index2.html', prediction_text= 'Your should choose {}' . format(prediction[0]) ) 
    

if __name__ == '__main__':
    app.run(debug=True)
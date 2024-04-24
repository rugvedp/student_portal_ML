from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import json
from youtubesearchpython import VideosSearch

def search_youtube_videos(topic, max_results=6):
    videosSearch = VideosSearch(topic, limit=max_results)
    result = videosSearch.result()
    videos = []
    for video in result['result']:
        video_data = {
            "title": video['title'],
            "url": video['link'],
            "views": video['viewCount']['short'],
            "duration": video['duration'],
            "thumbnail": video['thumbnails'][0]['url']
        }
        videos.append(video_data)
    return videos

with open('interest.json', 'r') as f:
    recommend = json.load(f)


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
    enigneer = None
    for item in recommend:
        if item['interest'] == prediction[0]:
            enigneer = item
            break
    print(enigneer)
    
    
    search = prediction[0] + 'roadmap'
    videos = search_youtube_videos(search)
    return render_template('index2.html',videos=videos, data=item) 
    

if __name__ == '__main__':
    app.run(debug=True)
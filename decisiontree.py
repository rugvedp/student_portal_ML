import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import sys

arguments = sys.argv[1:]

data = pd.read_csv("students11.csv")
label_encoder = LabelEncoder()

domains = LabelEncoder()
domains.fit(data['Interested Domain'])

majors = LabelEncoder()
majors.fit(data['Major'])

future = LabelEncoder()
future.fit(data["Future Career"])

projects = LabelEncoder()
projects.fit(data["Projects"])

encodeddata = data.copy()
encodeddata["Major"] = label_encoder.fit_transform(data["Major"])
encodeddata["Interested Domain"] = label_encoder.fit_transform(data["Interested Domain"])
encodeddata["Future Career"] = label_encoder.fit_transform(data["Future Career"])
encodeddata["Projects"] = label_encoder.fit_transform(data["Projects"])

data.drop("GPA", axis=1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(encodeddata[["Major", "Interested Domain", "Projects"]], encodeddata["Future Career"], test_size=0.25, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = (y_pred == y_test).mean()

sample_student_data = [[majors.transform(["Computer Science"])[0], domains.transform([arguments[0]])[0], projects.transform([arguments[1]])[0]]]
prediction = clf.predict(sample_student_data)
predicted_career = future.inverse_transform(prediction)
print(predicted_career[0])
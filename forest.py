import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import sys

arguments = sys.argv[1:]
data = pd.read_csv("students1111.csv")

le_major = LabelEncoder()
le_domain = LabelEncoder()
le_projects = LabelEncoder()

subject_values = {
    "Strong": 2,
    "Average": 1,
    "Weak": 0
}

data["Major"] = le_major.fit_transform(data["Major"])
data["Interested Domain"] = le_domain.fit_transform(data["Interested Domain"])
data["Projects"] = le_projects.fit_transform(data["Projects"])

data["Python"] = data["Python"].apply(lambda x: subject_values[x])
data["SQL"] = data["SQL"].apply(lambda x: subject_values[x])
data["Java"] = data["Java"].apply(lambda x: subject_values[x])

encoded_major = le_major.transform(["Computer Science"])
encoded_domain = le_domain.transform([arguments[0]])
encoded_projects = le_projects.transform([arguments[1]])

X_train, X_test, y_train, y_test = train_test_split(data[["Major", "Interested Domain", "Projects", "Python", "SQL", "Java"]], data["Future Career"], test_size=0.25, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = (y_pred == y_test).mean()

new_sample = [encoded_major, encoded_domain, encoded_projects, arguments[2], arguments[3], arguments[4]]
predicted_class = clf.predict([new_sample])
print(predicted_class[0])
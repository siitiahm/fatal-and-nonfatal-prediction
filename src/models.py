import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("PoliceKillingsUS-5000.csv")

# Encode feature values to numbers
le_armed = LabelEncoder()
le_age = LabelEncoder()
le_gender = LabelEncoder()
le_race = LabelEncoder()
le_illness = LabelEncoder()
le_threat = LabelEncoder()
le_flee = LabelEncoder()
le_cam = LabelEncoder()

inputs = df.drop('Fatal',axis='columns')
label = df['Fatal']

inputs['armed_n'] = le_armed.fit_transform(inputs['armed'])
inputs['age_n'] = le_age.fit_transform(inputs['age'])
inputs['gender_n'] = le_gender.fit_transform(inputs['gender'])
inputs['race_n'] = le_race.fit_transform(inputs['race'])
inputs['signs_of_mental_illness_n'] = le_illness.fit_transform(inputs['signs_of_mental_illness'])
inputs['threat_level_n'] = le_threat.fit_transform(inputs['threat_level'])
inputs['flee_n'] = le_flee.fit_transform(inputs['flee'])
inputs['body_camera_n'] = le_cam.fit_transform(inputs['body_camera'])

inputs_n = inputs.drop(['armed','age','gender','race','signs_of_mental_illness','threat_level','flee','body_camera'],axis='columns')
#inputs_n = inputs.drop(['armed','age','gender','race','signs_of_mental_illness'],axis='columns')

# Split data into training (70%) and testing (30%)
xtrain, xtest, ytrain, ytest = train_test_split(inputs_n, label, test_size=0.3, random_state=1, shuffle=True)

# DECISION TREE
dt_model = tree.DecisionTreeClassifier()
dt_model = dt_model.fit(xtrain, ytrain)
prediction = dt_model.predict(xtest)
print("DT accuracy: ", metrics.accuracy_score(ytest, prediction))

# EXTRA TREES
et_model = ExtraTreesClassifier()
et_model.fit(xtrain, ytrain)
et_pred = et_model.predict(xtest)
print("ET accuracy: ", metrics.accuracy_score(ytest, et_pred))

# RANDOM FOREST
rf = RandomForestClassifier(n_estimators = 1000, random_state = 42)
rf.fit(xtrain,ytrain)
prediction3 = rf.predict(xtest)
print("RF accuracy: ", metrics.accuracy_score(ytest, prediction3))

# LOGISTIC REGRESSION
lrmodel = LogisticRegression(max_iter=400)
lrmodel.fit(xtrain,ytrain)
lrmodel.predict(xtest)
score = lrmodel.score(xtest,ytest)
print("LR accuracy: ", score)

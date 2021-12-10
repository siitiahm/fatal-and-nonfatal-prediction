import pandas as pd
from sklearn.preprocessing import LabelEncoder

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

df = pd.read_csv("policekilling.csv")
df.head()

inputs = df.drop('Fatal',axis='columns')
target = df['Fatal']

print(inputs)

inputs['armed_n'] = le_company.fit_transform(inputs['armed'])
inputs['age_n'] = le_job.fit_transform(inputs['age'])
inputs['gender_n'] = le_degree.fit_transform(inputs['gender'])
inputs['race_n'] = le_company.fit_transform(inputs['race'])
inputs['signs_of_mental_illness_n'] = le_job.fit_transform(inputs['signs_of_mental_illness'])
inputs['threat_level_n'] = le_degree.fit_transform(inputs['threat_level'])
inputs['flee_n'] = le_degree.fit_transform(inputs['flee'])
inputs['body_camera_n'] = le_degree.fit_transform(inputs['body_camera'])


inputs_n = inputs.drop(['armed','age','gender','race','signs_of_mental_illness','threat_level','flee','body_camera'],axis='columns')

from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)
model.score(inputs_n,target)
#model.predict([[2,1,0]])

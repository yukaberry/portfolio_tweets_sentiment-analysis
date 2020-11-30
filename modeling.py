import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from feature_engneering import data_stack
import pickle
from sklearn import metrics

df = pd.read_csv("data/clean.csv")

"""separate features and labels"""
X = data_stack
y= df['Sentiment']

"""Split data into train and test"""
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42,stratify=y)

"""Modeling and see result"""
LogReg = LogisticRegression(random_state=42)
LogReg.fit(X_train,y_train)
predictions = LogReg.predict(X_test) 

print(metrics.accuracy_score(predictions,y_test))
print(metrics.classification_report(predictions,y_test))

"""save the model to disk"""
pickle_model = 'models/finalized_model.sav'
pickle.dump(LogReg, open(pickle_model, 'wb'))

"""load the model from disk and fit test data"""
loaded_model = pickle.load(open(pickle_model, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)

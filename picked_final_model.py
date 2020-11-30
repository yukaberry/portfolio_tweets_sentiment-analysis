import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from utils.data_cleaning_utils import addt_var_for_model
from utils.data_cleaning_utils import combine_feature_dfs


df = pd.read_csv("data/processed/negative_or_not_negative_df.csv")

# 2 gram max TF-IDF
tfidf_vectorizer = TfidfVectorizer(ngram_range = (1,2), sublinear_tf = True)

# TF-IDF feature matrix
tfidf = tfidf_vectorizer.fit_transform(df["toke_stem_stop"])

textToVectors = TfidfVectorizer(use_idf=True) # check tweets # To fix 
transformed = textToVectors.fit_transform(df["toke_stem_stop"])
vocab = textToVectors.fit(df["toke_stem_stop"]).vocabulary_

# Standardization numeric variables
num_features=["RetweetCount","FavoriteCount","followers"]

for col in num_features:
    scaler = MinMaxScaler()
    df[col] = scaler.fit_transform(np.array(df[col].values).reshape(-1, 1))

# Create final datasets for modeling
addt_vars_df = addt_var_for_model(df,num_features)
data_stack = combine_feature_dfs(tfidf, addt_vars_df)

# Split X and y values
X = data_stack
y= df['Sentiment_negative']


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42,stratify=y)

# Pass turned hyperparameters
log_ran = LogisticRegression(C =2.28024468035746, dual=False, penalty= 'l2', solver='lbfgs')
log_ran.fit(X_train,y_train)
y_pred = log_ran.predict(X_test)

# save a model
pickle_model = 'models/finalized_model_log.sav'
pickle.dump(log_ran, open(pickle_model, 'wb'))

# load picked model
loaded_model = pickle.load(open(pickle_model, 'rb'))
result = loaded_model.score(X_test, y_test)
print("result of base dataset")
print(result)
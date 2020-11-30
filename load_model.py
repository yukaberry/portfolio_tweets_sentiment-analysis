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
import pdb; pdb.set_trace()

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


"""train dataset""" 

df1 = pd.read_csv("data/processed/clean_ber.csv")

# 2 gram max TF-IDF
tfidf_vectorizer1 = TfidfVectorizer(ngram_range = (1,2), sublinear_tf = True)

# TF-IDF feature matrix
tfidf1 = tfidf_vectorizer1.fit_transform(df1["tidy_tweet"])

textToVectors1 = TfidfVectorizer(use_idf=True) 
transformed1 = textToVectors1.fit_transform(df1["tidy_tweet"])
vocab1 = textToVectors1.fit(df1["tidy_tweet"]).vocabulary_

# Standardization numeric variables
num_features1=["RetweetCount","FavoriteCount","followers"]

for col1 in num_features1:
    scaler1 = MinMaxScaler()
    df1[col] = scaler1.fit_transform(np.array(df1[col].values).reshape(-1, 1))

# Create final datasets for modeling
addt_vars_df1 = addt_var_for_model(df1,num_features1)
data_stack1 = combine_feature_dfs(tfidf1, addt_vars_df1)

# Split X and y values
X1 = data_stack1
y1 = df1['Sentiment']

# Split data
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1,random_state=42,stratify=y1)

# test Berlin  
result1 = loaded_model.score(X_test1, y_test1)
import pdb; pdb.set_trace()
print("result of Berlin dataset")
print(result1)







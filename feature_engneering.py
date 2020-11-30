import numpy as np
import pandas as pd
import string
import nltk
from utils.data_cleaning_utils import addt_var_for_model
from utils.data_cleaning_utils import combine_feature_dfs
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("data/clean.csv")

"""TF-IDF"""
bow_vectorizer = CountVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words='english')
# bag-of-words feature matrix
bow = bow_vectorizer.fit_transform(df['tidy_tweet'])

tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words='english')
# TF-IDF feature matrix
tfidf = tfidf_vectorizer.fit_transform(df['tidy_tweet'])

textToVectors = TfidfVectorizer(use_idf=True) # check  reviews on slak # To fix 
transformed = textToVectors.fit_transform(df['tidy_tweet'])
vocab = textToVectors.fit(df['tidy_tweet']).vocabulary_

"""Standardization numeric variables"""
num_features=["RetweetCount","FavoriteCount","followers"]

for col in num_features:
    scaler = MinMaxScaler()
    df[col] = scaler.fit_transform(np.array(df[col].values).reshape(-1, 1))


"""Create final datasets for modeling"""
addt_vars_df = addt_var_for_model(df,num_features)
data_stack = combine_feature_dfs(tfidf, addt_vars_df)

print(data_stack)






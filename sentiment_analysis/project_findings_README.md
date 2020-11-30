# Travel Sentiment Analysis Post COVID19


After many countries in Europe started to ease their lockdown and border restrictions on mid June in 2020, analysing a polarity of going traveling in summer 2020  during COVID19 will be beneficial for a business in tourism although there would be multiple other factors that will influence people to be able to travel for a holdiay.

In this page, it will explain findings of the project."How do pepople feel about traveling in summer 2020 during COVID19?" is the qustion I have set to answer by machine learning model.

# Table contents

1. Data extraction and labeling
2. Assumption
3. Exploring and cleaning data
4. Feature engneering
5. Modeling
6. Analysing sentiment
7. Challenges and augmentations



# 1. Data extraction

* Used tweepy and "Standard Search API " (I used a free version with limited functions but there are paid verisions which have more options [here to see more details](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/overview)).
* Extracted tweets on mid July 2020 which contains keywords ; *"corona" and "travel"*.  
* [Tweets objects](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object) : tweets, user id, time and date, the number of retweets, likes and followers. 
* Set to exclude retweets of tweets so a model can be fed by many variety of tweets. 
* English is a must language to extract tweets.


## 1.2 Labeled data by hand 

* There are two majoir ways to label data. 1. Use pre-trained model to label data or 2. Read every single tweets and label the porarity manually.
I chose to label data manually because there will not be any bias to the datasets. I would need a pre-trained model which were trained to build with travel data or similar concept of data to have accurate labelling outcome. What data were ded to a pre-trained model will be crucial to make a dataset from scratch. 

* Removed unrelated tweets for this project, such as adds or complaints about travel agencies/airlines and claiming for a refund

* 3 Categories 
  - 0 : Positive openions to go travelling at present.
  - 1 : Neutral tweets which show wish to travel but not at the moment. 
  - 2 : Negative for travelling.


## 1.3 Hide API keys and credentials 

* API keys and credentials should be kept secure because publicly exposing your credentials can result in your account being compromised, which could lead to unexpected charges on your account. 


![hide_keys](/image/hide_keys.PNG)


# 2. Assumption

I assumed that the majority of tweets are neutral including myself, I would tweet like " I wish to go on a holiday but my plan is cancelled due to corona....". WHile labeling the data, I noticed that there are quite a few tweets that indicated their holiday were cancelled or postponed but they want to start travelling when COVID situation was calm down a bit. Technically people would be able to travel since the borders are opened again. However, they seemes to keep eyes on the situation and figure out the right timing to travel. 


# 3. Exploring Data 

* There are 2 different types of datasets. *Type A* is for feeding a model as training datasets as well as test accuracy. *Type B* is only for testing polarity so it has not been labeled. I created 5 datasets in total. The final model was trained by [negative_or_not_negative_df.csv](/data/processed/negative_or_not_negative_df.csv). This dataset is balanced and has 2 labels instead of multi labels.


## 3.2 Type A
## 1 [clean.csv](/data/processed/clean.csv) 
* Size : 482 observations
* Label : "positive", "neutral", "negative"


### Small dataset and imbalanced 
higly imbalanced. Size of data is relatively small due to standard version of Twitter API and I suppose keywords I set.
#### Multi label : 0 = positive, 1 = neutral(wish to go travelling but not now), 2 = negative 

### Data balance

![data_balance](/image/data_balance.PNG)


### Favorite tweets
Negative tweets received "likes" the most.


![favo](/image/favo.PNG)


### Retweets and Followers
Singnificanly less negative tweets from users who have many followers. Most of retweets'sentiment is neutral considering negative tweets are majority. 

![retweet](/image/retweet.PNG)

![followers](/image/followers.PNG)

### User location
* "Place" columns is mostly NaN, so used "UserLocation" columns instead. 
* "Userlocation" is not so informative since users can register and express it in their own way. They are not names of countries or places. (ex: "moon", "world" etc) 
* The best solution will be to use upgraded version or get lattitude and longitude to analyse their locations if locations matter for further studies.

![userlocation](/image/tweets_location_barchart.png)


### 10 Most Frequest words of the initial dataset

![freq](/image/freq.PNG)



## 2 [negative_or_not_negative_df.csv](/data/processed/negative_or_not_negative_df.csv) 
* Resampled dataset from [clean.csv](/data/prcessed/clean.csv). The final model was fed by this dataset. 
* Size : 428 observations
* Label : "negative" or "not negative". I conbined positive and neutral as "not negative".

![negative_or_not_negative_balance_data](/image/negative_or_not_negative_balance_data.PNG)



![twitter_wc](/image/tw2.png)


## 3.3 Type B
### 3 [Tweets from Berlin](/data/processed/clean_ber.csv)
Size : 17 observations

![ber_wc](/image/ber.png)

### 4 [Tweets from New York](/data/processed/clean_nyr.csv)
Size : 113 observations


![ny_wc](/image/ny.png)

### 5 [Tweets from Melbourne](/data/processed/mel_clean.csv) 
Size : 9 observations

![roo_wc](/image/roo.png)



# 3.4 Cleaning data

* Removed "User account", "url","Punctuations", "Numbers", and "Special Characters".
* Removed Stopwords for this project because they act like noise for tf-idf method.
* Applied tokenising and stemming.
* There was no missing raw of tweet, also all in English. 


# 4. Feature engneering 

* Standraised (transform numbers between 0 to 1)  numeric varilable (the number of retweets, likes and followers) to be able to use with tf-idf feature.
* Tweets are converted as tf-idf.


# 5. Modeling

### Models' scores

3 different models (Logistic Regression, SVM, Random Forest) Random Forest perfomes the best in accuracy and Macro-F1

![forest](/image/result.PNG)


### Evaluation of the model

This Random Forest model is good at predicting negative tweets. There are room for improvement of poisive and neutral. The model classifies incorrectly in negative.

![forest](/image/randomforest_confusionM.PNG)



# 5.2 Modeling with resampled and binary datasets

Since the first dataset was highly imbalanced, I creaeted differen dataset([negative_or_not_negative_df.csv](/data/prcessed/negative_or_not_negative_df.csv) ). It brought a better outcome as below. This data set is used for building the final model. 


### Evaluation and Final Model

3 different models (Logistic Regression, SVM, Random Forest) Raandom Forest perfomes the best in accuracy and F1. F1 score was boosted by around 25%. All of the models perform much better in this dataset.
To select the final model, confusion matrix will help to make a decision. This will depend on what you would like to classify. SVC performes the best for classifying "Negative" class(94%), but this could also return negative result becuase False Negative rate is really high(61%). This means that the 61 % of times, this model will incorrectly classify "Not Negative" as "Negative". If the roject priority is to detect "not negative", this model will be not so useful like False Alarm projects.
Random Forest model works better to classify "True Positive" than SVC model. However, 48 % of times, this will return False Negative. 

Whereas Logistic Regression has balanced prediction accuracy in both F1 and accuracy as well as low False Positive rate. I chose **the final model as Logistic Regression** because I would like to see the balanced results of the customers' polarity.


![insert a image of model accuracy comparison](/image/result_2.PNG)


![insert a image of confusion matrix_randomF](/image/randomforest_confusionM_2.PNG)

![insert a image of confusion matrix_log](/image/log_confusionM_2.PNG)

![insert a image of confusion matriz_svm](/image/svm_confusionM_2.PNG)



# 5.3 What words make the difference of polarity? 

The chart shows the 30 largest and 30 smallest coefficients of the Logistic Regression model.The blue bar indicates "Not Negative", on the other hand the red bar indicates "Negative".

![negative_or_not_negative_impotant_words](/image/negative_or_not_negative_impotant_words.PNG)



# 6 Analysing the final model accuracy of 3 different locations


This results shows that "what data was the model trained by?" is important. [clean.csv](/data/processed/clean.csv) ([User location](/image/tweets_location_barchart.png)) does not have many tweets from Australia, thus, Melbourne's accuracy is the lowest in 3. Having said that, data size is small. Before concluding, I would like to test on a bigger dataset to see if this result below is reliable. 

![test_loc](/image/test_location_datasets_updated.PNG)



# 7 Challenges and Augmentations

* Not enough positive tweets by using search words I set. I could set up different search words to extract tweets for this project. Such as jus only "holiday", for instance. Two search words might have limited to the number of tweets. 
* It was difficult to get enought tweets from certain locations. When you set small Radius circles, it will be from an accurate location but inadequate. If you set larger range, the quantity will be satisfactory, however, tweets' locations includes other closer cities or countries.  
* Predicting neutral correctly was a challenge. I suppose that neutral was ambiguous.


### With additional time I would do the following:

* Try pre-trained model to label data to have larger datasets. 
* Improve "Macro F1 score" for multi label dataset by using wieght of some influenced/the mode frequent used words.
* Find out a factor of False Negative feature to improve the final model.
* Use a paid version of Twitter API for extract further history of tweets without limits. This would be useful to compare data in time series to see a curve of the trend.
* Try diffent models to analyse sentiment, such as LSTM’s or other models which capture the semantic meaning and the meaning of a word depends on the context of the previous text.





















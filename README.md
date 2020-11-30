# Project : NLP Sentiment Analysis

Using TwitterAPI and tweepy, extract tweets for sentiment analysis. "How do pepople feel about traveling during COVID19?" Tweets were extracted on July 2020. Analyse current customers' trend of 3 different locations (Melbourne, Berlin and New York). [sentiment_analysis](https://github.com/yukaberry/TwitterAPI2/tree/master/sentiment_analysis) demonstrates in more details.

* Data extraction
* Exploring and cleaning data
* Feature engneering
* Building models
* Analysing sentiment 


# Motivation
The study of tourist behaviour is crucial for travel industory after COVID19. I believe that forcasting customer trend and demand will have a great advantage for a business in tourism.


# Files' and folders' descriptions
### Folders
* [data]() Folder containing data files
  - [raw](https://github.com/yukaberry/TwitterAPI2/tree/master/data/raw) raw tweets data files
  - [processed](https://github.com/yukaberry/TwitterAPI2/tree/master/data/processed) labelled data files
* [image](https://github.com/yukaberry/TwitterAPI2/tree/master/image) Images used for [sentiment_analysis](https://github.com/yukaberry/TwitterAPI2/tree/master/sentiment_analysis)
* [models](https://github.com/yukaberry/TwitterAPI2/tree/master/models) Models saved for pickle
* [utils](https://github.com/yukaberry/TwitterAPI2/tree/master/utils) Utils folder
  - [data_cleaning_utils.py](https://github.com/yukaberry/TwitterAPI2/blob/master/utils/data_cleaning_utils.py) for cleaning tweets data, used in [data_cleaning.py](https://github.com/yukaberry/TwitterAPI2/blob/master/data_cleaning.py)
  - [data_extraction_utils.py](https://github.com/yukaberry/TwitterAPI2/blob/master/utils/data_extraction_utils.py) for extracting tweets, used in [api_data_retrieval.py](https://github.com/yukaberry/TwitterAPI2/blob/master/api_data_retrieval.py)

### Files
* [sentiment_analysis](https://github.com/yukaberry/TwitterAPI2/tree/master/sentiment_analysis) Analysing sentiments and model outcome by using graphs and images
* [api_data_retrieval.py](https://github.com/yukaberry/TwitterAPI2/blob/master/api_data_retrieval.py) Extract tweets (No location specify, it is for training datasets)
* [data_cleaning.py](https://github.com/yukaberry/TwitterAPI2/blob/master/data_cleaning.py) Cleaning train dataset using utils
* [feature_engneering.py](https://github.com/yukaberry/TwitterAPI2/blob/master/feature_engneering.py) Feature engneering: creating TF-IDF and normalized numeric variables





import json
import tweepy
import csv
import urllib
import time
import numpy as np
import pandas as pd
import os
from utils.data_extraction_utils import get_tweets_to_csv
from utils.data_extraction_utils import get_tweets_from_to_csv

auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_SECRET'))

api = tweepy.API(auth,wait_on_rate_limit=True)
#Error handling
if (not api):
    print ("Problem connecting to API")

"""Extract tweets"""
text_query = ["corona", "travel"]
tweet_items=1000
get_tweets_to_csv(text_query,tweet_items)


"""Extract tweets from certain locations"""
text_query=["corona","travel"]
tweet_items=400
geocodes= "52.49973,13.40338,400km" #Kreuzberg Berlin
get_tweets_from_to_csv(text_query,geocodes,tweet_items)
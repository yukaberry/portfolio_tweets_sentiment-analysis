

def get_tweets_to_csv(text_query,tweet_items):
   """ Get tweets, save them as DataFrame to a csv file. Retweet are excluded.

       parameters
       q: string, search term
       tweet_items: integer, set how many tweet you would like to get
       lang: string, language setting
       tweet_mode : integer, "extended" to see whole tweets in Dataframe
       result_type : integer, "recent" to get most recent tweets
   
   """
    tweet_list=[]
    for tweet in tweepy.Cursor(api.search, q=text_query,lang="en",tweet_mode="extended",result_type="recent",).items(tweet_items):
        if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
            tweet_list.append((tweet.user.location,tweet.place,tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count,tweet.user.followers_count,tweet.full_text))
            tweetsdf = pd.DataFrame(tweet_list,columns=['UserLocation','Place','Datetime', 'TweetId','RetweetCount','FavoriteCount','followers','Text'])
            tweetsdf.to_csv('data/raw/tweets_raw.csv'.format())


def get_tweets_from_to_csv(text_query,geocodes,tweet_items):
    """Get tweets from certain locations and  save them as DataFrame to a csv file. Retweet are excluded.

    Parameter:
    text_query = strings, can be a list like ["corona","travel"]
    q=text_query : needs to be exactly like this, otherwise it returns Error message :"text_query" is not defined.

    geocodes = latitude,longitude,radius
               "-37.8136,144.9631,100km" Melbourne, "51.50853, -0.12574,100km" London,
               "40.71427, -74.00597,100km" New York,"52.49973, 13.40338" Kreuzberg Berlin
               "52.205276, 0.119167." Cambridge " 42.407211, -71.382439." Massachusetts
               
                have enough "radius" to extract tweets, otherwise returns only a few tweets sometimes.

                
    tweet_items = integer, like 100. Note 100 means that 100 lines of info or something(not sure), NOT 100 tweets. 
    
    tweet_mode="extended" : to show whole tweets instead of limited character with twitter links.
    
    result_type='recent': you could replaced by until=2020-7-5 for example. TwitterAPI standard version can get 1 week of history tweets from today.
    
    
    """
    tweet_loc_list=[]
    try:
        for tweet in tweepy.Cursor(api.search, q=text_query,lang="en",tweet_mode="extended",result_type='recent',geocode=geocodes).items(tweet_items):
            
            #Remove Retweets for extracting training data. You could remove this part if it is for test data
            if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                
                # Adding to list that contains all tweets,To add more attriutes, refer to links on README
                tweet_loc_list.append((tweet.user.location,tweet.place,tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count,tweet.user.followers_count,tweet.full_text))
                
                # Creation of dataframe from tweets list
                tweets_loc_df = pd.DataFrame(tweet_loc_list,columns=['UserLocation','Place','Datetime', 'TweetId','RetweetCount','FavoriteCount','followers','Text'])
                
                # Converting dataframe to csv file, text_query will be the name of this csv file
                tweets_loc_df.to_csv('data/raw/tweets_raw_location.csv')
    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)









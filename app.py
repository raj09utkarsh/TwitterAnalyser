import tweepy
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
import Apis
# Comment out line 5

def func(search_query, n):
    ''' Delete Apis.ConsumerApiKey and Enter your consumer api key '''
    Consumer_Api_Key    = Apis.ConsumerApiKey    
    ''' Delete Apis.ConsumerSecret and Enter your consumer secret ''' 
    Consumer_Secret     = Apis.ConsumerSecret
    ''' Delete Apis.AccessToken and Enter your access token ''' 
    Access_Token        = Apis.AccessToken       
    ''' Delete Apis.AccessTokenSecret and Enter your access token secret '''
    Access_Token_Secret = Apis.AccessTokenSecret  


    auth = tweepy.OAuthHandler(Consumer_Api_Key, Consumer_Secret)
    auth.set_access_token(Access_Token, Access_Token_Secret)

    api = tweepy.API(auth)


    tweets = tweepy.Cursor(api.search, q=f'#{search_query}', tweet_mode = 'extended', lang='en', count = 100).items(n)


    pos = 0
    neg = 0
    neu = 0


    for tweet in tweets:
        blob = TextBlob(tweet.full_text)
        polarity = blob.sentiment.polarity
        if polarity == 0:
            neu += 1
        elif polarity < 0.00:
            neg += 1
        elif polarity > 0.00:
            pos += 1


    pos_percentage = (pos/n)*100
    neg_percentage = (neg/n)*100
    neu_percentage = (neu/n)*100

    print(f'{pos} persons tweeted positive, {neg} persons tweeted negative and {neu} persons were neutral')

    pos_percentage = format(pos_percentage, '.2f')
    neg_percentage = format(neg_percentage, '.2f')
    neu_percentage = format(neu_percentage, '.2f')


    # Plot using Matplotlib
    label = [f'Positive [{str(pos_percentage)}%]', f'Negative [{str(neg_percentage)}%]', f'Neutral [{str(neu_percentage)}%]']
    sizes = [pos, neg, neu]
    colors = ['yellowgreen', 'blue', 'red']

    patches, texts = plt.pie(sizes, colors=colors, startangle=90)

    plt.legend(patches, label, loc = 'best')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    search_query = input("Enter the hashtag you want to search for: ")
    n = int(input('Enter number of tweets you want to analyse: '))
    func(search_query, n)
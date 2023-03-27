import tweepy
import pandas as pd
pd.set_option('max_columns', None)
pd.set_option('display.width', 500)

api_key = "CJSz41qVbb9ENG6R3J75YiU9e"
api_secret = "KY2WejXPfs6p1dSI4IELWrUhhZzIfUPLyzGKQMZKjVcaDisXCt"
access_token = "4055771794-lkkxIe1fn2PIoTYEYKK3Kp1Zixh3rHM583QN61a"
access_token_secret = "lYigp4octqNxOOgNnDRJdTxiuYefhqswmgyoWq4wRQGOU"

# authenticate with the API
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')

except:
    print('Failed authentication')

# Set the function parameters:
query = "#elonmusk"
lang = "en"
tweet_mode = "extended"
count = 20
tweet_limit = 30


# Define the scraping function:
def tweet_scraper(query=None, lang="en", tweet_mode="extended", count=100, tweet_limit=1000):
    # Data dictionary for collecting results:
    data = {
        "tweet_id": [],
        "created_at": [],
        "full_text": [],

    }

    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode=tweet_mode, count=count)\
            .items(tweet_limit):
        # Tweet ID:
        data["tweet_id"].append(tweet.id)
        # Date:
        data["created_at"].append(tweet.created_at)
        # Full text of tweet:
        data["full_text"].append(tweet.full_text)

    df = pd.DataFrame(data)

    return df


df = tweet_scraper(query=query, lang=lang, tweet_mode=tweet_mode, count=count, tweet_limit=tweet_limit)

# Save our results:
df.to_csv('twitter_data.csv', index=False)

print(df)

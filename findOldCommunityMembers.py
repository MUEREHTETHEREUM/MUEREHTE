"""
Purpose of the Script:
-----------------------
This script is designed to search Twitter for mentions of the "$HTE" hashtag and collect the Twitter handles of those who have tweeted about it. It prioritizes tweets over replies and is limited to the first 1500 tweets to stay within the specified limit. The script uses the Tweepy library to interface with the Twitter API, ensuring efficient and accurate retrieval of data. This can be useful for tracking engagement, analyzing sentiment, or building a community around the MUEREHTE coin.
"""
import tweepy

# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate with Twitter's API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define the search query to find tweets mentioning "$HTE"
search_query = "$HTE -filter:retweets"  # Excluding retweets

# List to store unique Twitter handles
twitter_handles = []

# Search and process tweets
for tweet in tweepy.Cursor(api.search, q=search_query, lang="en", tweet_mode="extended").items(1500):
    handle = tweet.user.screen_name  # Extract the Twitter handle
    if handle not in twitter_handles:  # Avoid duplicates
        twitter_handles.append(handle)

# Print the collected Twitter handles
for handle in twitter_handles:
    print(handle)

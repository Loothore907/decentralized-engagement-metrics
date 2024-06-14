import tweepy
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# Load Twitter API credentials from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Read the list of Twitter accounts from the CSV file
accounts_df = pd.read_csv('twitter_accounts.csv')
accounts = accounts_df['username'].tolist()

# Function to fetch the last 5 tweets of a user
def fetch_last_5_tweets(username):
    tweets = api.user_timeline(screen_name=username, count=5, tweet_mode='extended')
    return tweets

# Function to fetch the last 5 responses to a tweet
def fetch_last_5_responses(tweet_id):
    responses = api.search_tweets(q='to:{}'.format(tweet_id), since_id=tweet_id, tweet_mode='extended', count=5)
    return responses

# Initialize a DataFrame to store the results
columns = ['Account Posting', 'Post', 'Account Responding', 'Response', 'Post Date', 'Response Date']
data = pd.DataFrame(columns=columns)

# Loop through each account and fetch data
for account in accounts:
    tweets = fetch_last_5_tweets(account)
    for tweet in tweets:
        tweet_id = tweet.id
        tweet_text = tweet.full_text
        tweet_date = tweet.created_at

        responses = fetch_last_5_responses(tweet_id)
        for response in responses:
            response_text = response.full_text
            response_date = response.created_at
            response_account = response.user.screen_name

            # Check for duplicates (simplified check)
            if not ((data['Post'] == tweet_text) & (data['Response'] == response_text)).any():
                new_row = {
                    'Account Posting': account,
                    'Post': tweet_text,
                    'Account Responding': response_account,
                    'Response': response_text,
                    'Post Date': tweet_date,
                    'Response Date': response_date
                }
                data = data.append(new_row, ignore_index=True)

# Save the collected data to a CSV file
data.to_csv('twitter_data.csv', index=False)

print("Data collection complete. Saved to twitter_data.csv")

import os
import csv
import tweepy
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import sys

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logger import setup_logger

# Initialize logger
logger = setup_logger(__name__)

# Load environment variables
load_dotenv()

# Correct environment variable names
TWITTER_API_KEY = os.getenv('CONSUMER_KEY')
TWITTER_API_SECRET_KEY = os.getenv('CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Check if any of the keys are None
if not all([TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET]):
    raise ValueError("One or more Twitter API credentials are missing. Please check your .env file.")

# Configure Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

async def fetch_tweets(username):
    try:
        tweets = api.user_timeline(screen_name=username, count=100, tweet_mode="extended")
        logger.info(f"Fetched {len(tweets)} tweets for {username}")
        return tweets
    except Exception as e:
        logger.error(f"Error fetching tweets for {username}: {e}")
        return []

async def fetch_all_tweets(usernames):
    tasks = [fetch_tweets(username) for username in usernames]
    results = await asyncio.gather(*tasks)
    return results

def load_usernames(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tweets_to_file(tweets, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['username', 'tweet_id', 'created_at', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user_tweets in tweets:
            for tweet in user_tweets:
                writer.writerow({
                    'username': tweet.user.screen_name,
                    'tweet_id': tweet.id,
                    'created_at': tweet.created_at,
                    'text': tweet.full_text
                })

def main():
    project_usernames = load_usernames(os.path.join(os.path.dirname(__file__), 'jupiter_project_accounts.csv'))
    community_usernames = load_usernames(os.path.join(os.path.dirname(__file__), 'jupiter_community_accounts.csv'))
    
    loop = asyncio.get_event_loop()
    
    project_tweets = loop.run_until_complete(fetch_all_tweets(project_usernames))
    community_tweets = loop.run_until_complete(fetch_all_tweets(community_usernames))
    
    save_tweets_to_file(project_tweets, 'project_tweets.csv')
    save_tweets_to_file(community_tweets, 'community_tweets.csv')
    
    logger.info("Fetched tweets for all project and community accounts")

if __name__ == "__main__":
    main()

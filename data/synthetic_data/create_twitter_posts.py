import os
import random
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Set up the OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the script directory and output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir)

# Debug: Print the directories
print(f"Script Directory: {script_dir}")
print(f"Output Directory: {output_dir}")

# Define dynamic prompts for generating tweets
crypto_prompt = "You are a social media expert. Create 10 tweets about known crypto projects, each tweet on a new line, with at least half about Jupiter DAO and its ecosystem."
general_prompt = "You are a social media expert. Create 10 non-crypto tweets that include personal experiences, product announcements, project updates, and humorous commentary, each tweet on a new line."

# Function to generate tweets using GPT-3.5-turbo
def generate_tweets_with_context(prompt, n=10):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a social media expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,  # Allow enough tokens for 10 tweets
        temperature=0.7
    )
    content = response.choices[0].message.content.strip()
    tweets = content.split('\n')[:n]  # Assume tweets are separated by newlines
    # Debug: Print the generated content
    print(f"Generated content:\n{content}\n")
    print(f"Split tweets: {tweets}")
    return tweets

# Function to generate and save tweets
def generate_and_save_tweets(prompt, filename, tweet_type, num_loops=100, mode='a'):
    all_tweets = []
    for i in range(num_loops):
        print(f"Loop {i+1}/{num_loops} for {tweet_type} tweets")
        tweets = generate_tweets_with_context(prompt, n=10)
        for tweet in tweets:
            if tweet:
                all_tweets.append({'tweet': tweet, 'type': tweet_type})
        print(f"Generated {len(tweets)} tweets for loop {i+1}")
    
    df = pd.DataFrame(all_tweets)
    # Debug: Print the total number of tweets generated
    print(f"Total {tweet_type} tweets generated: {len(all_tweets)}")
    # Debug: Print the filename before saving
    print(f"Saving to {filename}")
    df.to_csv(filename, mode=mode, header=not os.path.exists(filename), index=False)
    print(f"Synthetic tweets saved to {filename}")

# Generate and save crypto-related tweets
generate_and_save_tweets(crypto_prompt, os.path.join(output_dir, 'synthetic_crypto_twitter.csv'), 'crypto')

# Generate and save general tweets
generate_and_save_tweets(general_prompt, os.path.join(output_dir, 'synthetic_traditional_twitter.csv'), 'traditional')

# Combine both datasets
crypto_df = pd.read_csv(os.path.join(output_dir, 'synthetic_crypto_twitter.csv'))
traditional_df = pd.read_csv(os.path.join(output_dir, 'synthetic_traditional_twitter.csv'))

combined_df = pd.concat([crypto_df, traditional_df])
combined_df.to_csv(os.path.join(output_dir, 'combined_twitter_dataset.csv'), index=False)
print("Combined dataset saved to data/synthetic_data/combined_twitter_dataset.csv")
print(f"Total combined tweets: {len(combined_df)}")

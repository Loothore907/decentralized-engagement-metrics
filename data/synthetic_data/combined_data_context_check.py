import os
import pandas as pd

# Define the script directory and output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir)

# Load the combined dataset
combined_dataset_path = os.path.join(output_dir, 'combined_twitter_dataset.csv')
combined_df = pd.read_csv(combined_dataset_path)

# Sample a subset of the dataset for manual inspection
sample_df = combined_df.sample(20)
print(sample_df)

# Automated context check
def context_check(tweet, keywords):
    return any(keyword.lower() in tweet.lower() for keyword in keywords)

# Define keywords for context check
crypto_keywords = ['Jupiter DAO', 'crypto', 'DeFi', 'blockchain']
traditional_keywords = ['coffee', 'product', 'marketing', 'experience']

# Add a context relevance column
combined_df['context_relevant'] = combined_df.apply(
    lambda row: context_check(row['tweet'], crypto_keywords) if row['type'] == 'crypto' else context_check(row['tweet'], traditional_keywords),
    axis=1
)

# Calculate the percentage of contextually relevant tweets
relevance_percentage = combined_df['context_relevant'].mean() * 100
print(f"Percentage of contextually relevant tweets: {relevance_percentage:.2f}%")

# Save the inspected dataset
inspected_dataset_path = os.path.join(output_dir, 'inspected_twitter_dataset.csv')
combined_df.to_csv(inspected_dataset_path, index=False)
print(f"Inspected dataset saved to {inspected_dataset_path}")

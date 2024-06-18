import os
import pandas as pd

# Define the script directory and output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir)

# Load the inspected dataset
inspected_dataset_path = os.path.join(output_dir, 'inspected_twitter_dataset.csv')
df = pd.read_csv(inspected_dataset_path)

# Display summary statistics
print(df['context_relevant'].value_counts())
print(f"Total tweets: {len(df)}")
print(f"Contextually relevant tweets: {df['context_relevant'].sum()}")
print(f"Percentage of contextually relevant tweets: {df['context_relevant'].mean() * 100:.2f}%")

# Group by type and context relevance
context_by_type = df.groupby(['type', 'context_relevant']).size().unstack(fill_value=0)
print(context_by_type)

# Sample some contextually relevant and non-relevant tweets for manual review
relevant_sample = df[df['context_relevant']].sample(10)
non_relevant_sample = df[~df['context_relevant']].sample(10)

print("Sample of contextually relevant tweets:")
print(relevant_sample)

print("\nSample of non-relevant tweets:")
print(non_relevant_sample)

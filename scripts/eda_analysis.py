import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/ecommerce_behavior_cleaned.csv")

# Clean data (example)
df.dropna(inplace=True)
df['event_time'] = pd.to_datetime(df['event_time'])
df['event_date'] = df['event_time'].dt.date

# Basic Analysis
print("Top product categories:\n", df['category_code'].value_counts().head())
print("\nConversion Rate:", df[df['event_type'] == 'purchase'].shape[0] / df.shape[0])

# Save clean data
df.to_csv("../output/cleaned_dataset.csv", index=False)

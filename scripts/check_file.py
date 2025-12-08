import pandas as pd

# FIRST: Read just the first few rows to understand structure
print("Reading first 5 rows to understand structure...")
sample = pd.read_csv('data/MachineLearningRating_v3.txt', 
                     nrows=5, 
                     sep='\t',  # try tab separator first
                     low_memory=False)

print("First 5 rows:")
print(sample)

print("\nColumns found:")
print(sample.columns.tolist())

print("\nFile structure:")
print(sample.info())

# If tab doesn't work, try comma
if len(sample.columns) == 1:
    print("\nTrying comma separator...")
    sample = pd.read_csv('data/MachineLearningRating_v3.txt', 
                         nrows=5, 
                         sep=',',
                         low_memory=False)
    print(sample.columns.tolist())
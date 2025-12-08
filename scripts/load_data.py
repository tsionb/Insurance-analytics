import pandas as pd
import numpy as np
from tqdm import tqdm
import os

def load_large_txt_file(file_path, chunk_size=100000):
    """
    Load large .txt file efficiently using chunking
    """
    print(f"Loading file: {file_path}")
    print(f"File size: {os.path.getsize(file_path) / (1024**3):.2f} GB")
    
    # First, let's check the structure
    print("\nChecking file structure...")
    
    # Read first few lines to understand structure
    with open(file_path, 'r') as f:
        first_lines = [next(f) for _ in range(5)]
    
    print("First 5 lines:")
    for i, line in enumerate(first_lines):
        print(f"Line {i+1}: {line[:100]}...")
    
    # Try to determine delimiter
    delimiters = [',', ';', '\t', '|']
    for delim in delimiters:
        sample = first_lines[0].split(delim)
        if len(sample) > 1:
            print(f"\nDetected delimiter: '{delim}'")
            print(f"Number of columns in first row: {len(sample)}")
            break
    
    # Now read in chunks
    print("\nReading data in chunks...")
    chunks = []
    for chunk in tqdm(pd.read_csv(file_path, 
                                  delimiter=delim,
                                  chunksize=chunk_size,
                                  low_memory=False)):
        chunks.append(chunk)
    
    # Combine chunks
    df = pd.concat(chunks, ignore_index=True)
    
    print(f"\nData loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
    
    return df

if __name__ == "__main__":
    # Load the data
    df = load_large_txt_file("data/MachineLearningRating_v3.txt")
    
    # Save a sample for quick testing
    df_sample = df.sample(min(10000, len(df)))
    df_sample.to_csv("data/insurance_sample.csv", index=False)
    print("\nSaved sample data to data/insurance_sample.csv")
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import time
import psutil
import os

def log_memory(stage: str):
    """Log memory usage at a given stage."""
    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / 1024 ** 2
    print(f"[Memory] {stage}: {memory_mb:.2f} MB")

def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in the DataFrame.
    Numeric columns are filled with mean, categorical columns with 'Unknown'.
    Logs memory usage and execution time.
    """
    start = time.time()
    # log_memory("before fill_missing")

    # Define numeric and categorical columns
    numeric_cols = ["age", "education_num", "hours_per_week"]
    categorical_cols = [
        "sex", "workclass", "education", "marital_status",
        "occupation", "relationship", "race", "native_country"
    ]

    # Fill missing numeric columns with mean
    for col in numeric_cols:
        if col in df.columns:
            df[col].fillna(df[col].mean(), inplace=True)

    # Fill missing categorical columns with "Unknown"
    for col in categorical_cols:
        if col in df.columns:
            df[col].fillna("Unknown", inplace=True)

    end = time.time()
    # print(f"[fill_missing] Done in {end - start:.2f} seconds")
    # log_memory("after fill_missing")

    return df

def main():
    start_time = time.time()

    # Step 1: Read CSV for the pipeline
    df = pd.read_csv("adult_income.csv")

    # Step 2: Fill missing values
    df = fill_missing(df)

    # Step 3: Save output for next stage
    df.to_csv("2_fill_missing_output.csv", index=False)
    print("[Info] Saved 2_fill_missing_output.csv")

    end_time = time.time()
    # print(f"[main] fill_missing stage completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

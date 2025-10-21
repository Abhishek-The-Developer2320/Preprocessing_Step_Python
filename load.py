import pandas as pd
import psutil
import os
import time

def log_memory(stage: str):
    """Log memory usage at a given stage."""
    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / 1024 ** 2  # Convert bytes to MB
    print(f"[Memory] {stage}: {memory_mb:.2f} MB")

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the CSV file and return a pandas DataFrame.
    Also saves a copy as '1_read_output.csv' for next stages.
    """
    start = time.time()
    df = pd.read_csv(file_path)
    end = time.time()
    # print(f"[Execution Time] Loading CSV: {end - start:.2f} seconds")

    # Save for next stage
    df.to_csv("1_read_output.csv", index=False)
    print("[Info] Saved 1_read_output.csv for next stage.")

    return df

def main():
    file_path = "adult_income.csv"
    df = load_data(file_path)
    print(f"[DataFrame] Loaded shape: {df.shape}")

if __name__ == "__main__":
    main()

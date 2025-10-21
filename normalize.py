import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import time

def normalize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize numeric columns using min-max scaling.
    """
    start_time = time.time()

    numeric_cols = ["age", "education_num", "hours_per_week"]

    for col_name in numeric_cols:
        if col_name in df.columns:
            min_val = df[col_name].min()
            max_val = df[col_name].max()
            df[col_name] = (df[col_name] - min_val) / (max_val - min_val)

    end_time = time.time()
    # print(f"[normalize] Done in {end_time - start_time:.2f} seconds")
    return df

def main():
    start_time = time.time()

    # Step 1: Read CSV from previous stage
    df = pd.read_csv("2_fill_missing_output.csv")

    # Step 2: Normalize
    df = normalize(df)

    # Step 3: Save to next stage CSV
    df.to_csv("3_normalized_output.csv", index=False)
    print("[Info] Saved 3_normalized_output.csv")

    end_time = time.time()
    # print(f"[main] normalize stage completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

import pandas as pd
import time

def clip_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clip numeric outliers to 1st and 99th percentiles.
    """
    start_time = time.time()

    numeric_cols = ["age", "education_num", "hours_per_week"]

    for col_name in numeric_cols:
        if col_name in df.columns:
            lower = df[col_name].quantile(0.01)
            upper = df[col_name].quantile(0.99)
            df[col_name] = df[col_name].clip(lower=lower, upper=upper)

    end_time = time.time()
    # print(f"[clip_outliers] Done in {end_time - start_time:.2f} seconds")
    return df

def main():
    start_time = time.time()

    # Step 1: Read CSV from previous stage
    df = pd.read_csv("4_income_encoded_output.csv")

    # Step 2: Clip numeric outliers
    df = clip_outliers(df)

    # Step 3: Save output
    df.to_csv("5_clipped_output.csv", index=False)
    print("[Info] Saved 5_clipped_output.csv")

    end_time = time.time()
    # print(f"[main] clip_outliers stage completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

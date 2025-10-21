import pandas as pd
import time

def one_hot_encode(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """
    One-hot encode a specific categorical column.
    Example for 'sex': creates 'sex_Male' and 'sex_Female' columns.
    """
    start_time = time.time()

    if col_name in df.columns:
        dummies = pd.get_dummies(df[col_name], prefix=col_name)
        df = pd.concat([df.drop(col_name, axis=1), dummies], axis=1)

    end_time = time.time()
    # print(f"[one_hot_encode] Done in {end_time - start_time:.2f} seconds")
    return df

def main():
    start_time = time.time()

    # Step 1: Read CSV from previous stage
    df = pd.read_csv("5_clipped_output.csv")

    # Step 2: One-hot encode the 'sex' column
    df = one_hot_encode(df, "sex")

    # Step 3: Save output
    df.to_csv("6_one_hot_output.csv", index=False)
    print("[Info] Saved 6_one_hot_output.csv")

    end_time = time.time()
    # print(f"[main] one_hot_encode stage completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

import pandas as pd
import time

def encode_income(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode the 'income' column into binary values.
    <=50K -> 0, >50K -> 1
    """
    start_time = time.time()

    if 'income' in df.columns:
        df['income_encoded'] = df['income'].apply(lambda x: 0 if x == '<=50K' else 1)

    end_time = time.time()
    # print(f"[encode_income] Done in {end_time - start_time:.2f} seconds")
    return df

def main():
    start_time = time.time()

    # Step 1: Read CSV from previous stage
    df = pd.read_csv("3_normalized_output.csv")

    # Step 2: Encode income column
    df = encode_income(df)

    # Step 3: Save output
    df.to_csv("4_income_encoded_output.csv", index=False)
    print("[Info] Saved 4_income_encoded_output.csv")

    end_time = time.time()
    # print(f"[main] encode_income stage completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

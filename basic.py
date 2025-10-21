import pandas as pd
import numpy as np
import time

start = time.time()

def log_memory(stage: str):
    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / 1024 ** 2  # Convert bytes to MB
    print(f"[Memory] {stage}: {memory_mb:.2f} MB")

log_memory("before loading")
# Load CSV
df = pd.read_csv("adult_income.csv")

# Define numeric and categorical columns
numeric_cols = ["age", "education_num", "hours_per_week"]
categorical_cols = ["sex", "workclass", "education", "marital_status", "occupation", 
                    "relationship", "race", "native_country"]

# Fill missing numeric columns with mean
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill missing categorical columns with "Unknown"
for col in categorical_cols:
    df[col].fillna("Unknown", inplace=True)

# Normalize numeric columns (Min-Max scaling)
for col in numeric_cols:
    min_val = df[col].min()
    max_val = df[col].max()
    df[col] = (df[col] - min_val) / (max_val - min_val)

# Clip outliers using IQR
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower, upper)

# One-hot encode 'sex'
df = pd.get_dummies(df, columns=["sex"], prefix="sex")

# Create income_level column
df["income_level"] = df["income"].apply(lambda x: "Low" if x == "<=50K" else "High")

# Filter rows where age > 0.5 (after normalization)
df = df[df["age"] > 0.5]

# Save cleaned CSV
df.to_csv("cleaned_us_census_python.csv", index=False)

end = time.time()
print(f"Done. Execution time: {end - start:.2f} seconds")
print(f"Memory used (approx): {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

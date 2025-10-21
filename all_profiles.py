import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import time
import psutil
import os
import pandas as pd

# Import your processing functions
from load import load_data
from fill_missing import fill_missing
from normalize import normalize
from clip_outlier import clip_outliers
from one_hot_encode import one_hot_encode
from new_col_income import encode_income

def profile_stage(stage_name, func, *args, **kwargs):
    """Generic profiler for a data processing stage."""
    start_time = time.time()
    process = psutil.Process(os.getpid())
    peak_mem_mb = 0

    # Execute the function
    result = func(*args, **kwargs)

    # Measure memory usage
    mem_mb = process.memory_info().rss / (1024 ** 2)
    peak_mem_mb = max(peak_mem_mb, mem_mb)

    end_time = time.time()
    execution_time = end_time - start_time

    # Print profiling summary
    print(f"================= Profiling: {stage_name} =================")
    print(f"Execution Time      : {execution_time:.2f} seconds")
    print(f"Peak Memory Usage   : {peak_mem_mb:.2f} MB")
    print("===========================================================")

    return result

def profile_load():
    return profile_stage("Load", load_data, "adult_income.csv")

def profile_fill_missing(df):
    return profile_stage("Fill Missing", fill_missing, df)

def profile_normalize(df):
    return profile_stage("Normalize", normalize, df)

def profile_clip_outliers(df):
    return profile_stage("Clip Outliers", clip_outliers, df)

def profile_one_hot_encode(df):
    return profile_stage("One-Hot Encode", one_hot_encode, df,"sex")

def profile_new_col_income(df):
    return profile_stage("New-Col Income", encode_income, df)

# Run the full pipeline
if __name__ == "__main__":
    df = profile_load()
    df = profile_fill_missing(df)
    df = profile_normalize(df)
    df = profile_clip_outliers(df)
    df = profile_one_hot_encode(df)
    df = profile_new_col_income(df)
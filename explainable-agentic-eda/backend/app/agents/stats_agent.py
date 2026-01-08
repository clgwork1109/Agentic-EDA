# Stats agent placeholder
import pandas as pd

def statistical_summary(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include="number")

    summaries = {}
    for col in numeric_df.columns:
        summaries[col] = {
            "mean": float(numeric_df[col].mean()),
            "std": float(numeric_df[col].std()),
            "min": float(numeric_df[col].min()),
            "max": float(numeric_df[col].max()),
            "skew": float(numeric_df[col].skew())
        }

    return summaries

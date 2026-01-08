# Quality agent placeholder
def assess_quality(df):
    return {
        "missing_ratio": float(df.isna().mean().mean()),
        "duplicate_rows": int(df.duplicated().sum())
    }

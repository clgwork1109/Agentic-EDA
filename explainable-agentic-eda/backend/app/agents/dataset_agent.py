# Dataset agent placeholder
def analyze_dataset(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numeric_columns": df.select_dtypes(include="number").columns.tolist(),
        "categorical_columns": df.select_dtypes(include="object").columns.tolist()
    }

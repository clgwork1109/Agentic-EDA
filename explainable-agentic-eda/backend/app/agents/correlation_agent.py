# Correlation agent placeholder
def correlation_matrix(df):
    numeric_df = df.select_dtypes(include="number")

    corr = numeric_df.corr().round(3)
    matrix = []

    cols = corr.columns.tolist()
    for i, row in enumerate(cols):
        for j, col in enumerate(cols):
            matrix.append([i, j, float(corr.iloc[i, j])])

    return {
        "columns": cols,
        "matrix": matrix,
        "method": "pearson"
    }

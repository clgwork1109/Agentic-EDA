import pandas as pd
from typing import Dict, Any
import os

class DatasetIngestionAgent:
    """
    Agent responsible for ingesting datasets from CSV or Excel files.
    Handles file loading, basic preprocessing for missing values, and provides dataset overview.
    """

    def __init__(self):
        pass

    def process(self, file_path: str) -> Dict[str, Any]:
        """
        Ingests the dataset from the given file path.

        Args:
            file_path (str): Path to the CSV or Excel file.

        Returns:
            Dict[str, Any]: Structured output containing the dataset and metadata.
                - 'data': pandas DataFrame
                - 'shape': tuple of (rows, columns)
                - 'columns': list of column names
                - 'dtypes': dict of column dtypes
                - 'missing_summary': dict of missing values per column
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext == '.csv':
            df = pd.read_csv(file_path)
        elif file_ext in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Only CSV and Excel are supported.")

        # Handle missing values safely: fill numerical with mean, categorical with mode or 'Unknown'
        for col in df.columns:
            if df[col].dtype in ['int64', 'float64']:
                df[col] = df[col].fillna(df[col].mean())
            else:
                mode_val = df[col].mode()
                fill_val = mode_val[0] if not mode_val.empty else 'Unknown'
                df[col] = df[col].fillna(fill_val)

        shape = df.shape
        columns = list(df.columns)
        dtypes = df.dtypes.to_dict()
        missing_summary = df.isnull().sum().to_dict()

        return {
            'data': df,
            'shape': shape,
            'columns': columns,
            'dtypes': dtypes,
            'missing_summary': missing_summary
        }
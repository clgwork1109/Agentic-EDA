import pandas as pd
from typing import Dict, Any, List

class SchemaSemanticsAgent:
    """
    Agent responsible for analyzing the dataset schema and inferring semantic meanings.
    Classifies columns into numerical, categorical, datetime, etc., and suggests roles.
    """

    def __init__(self):
        pass

    def process(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Analyzes the schema and semantics of the dataset.

        Args:
            data (pd.DataFrame): The ingested dataset.

        Returns:
            Dict[str, Any]: Structured output with column classifications and semantics.
                - 'column_types': dict mapping column names to types ('numerical', 'categorical', 'datetime', 'text')
                - 'potential_targets': list of potential target columns for modeling
                - 'key_insights': list of strings with semantic insights
        """
        column_types = {}
        potential_targets = []
        key_insights = []

        for col in data.columns:
            dtype = data[col].dtype
            unique_vals = data[col].nunique()
            total_vals = len(data[col])

            if pd.api.types.is_numeric_dtype(dtype):
                if unique_vals / total_vals < 0.05:  # less than 5% unique, treat as categorical
                    column_types[col] = 'categorical'
                else:
                    column_types[col] = 'numerical'
                    if col.lower() in ['target', 'label', 'y', 'class']:
                        potential_targets.append(col)
            elif pd.api.types.is_datetime64_any_dtype(dtype) or 'date' in col.lower() or 'time' in col.lower():
                column_types[col] = 'datetime'
            elif dtype == 'object':
                if unique_vals / total_vals < 0.1:  # low uniqueness, categorical
                    column_types[col] = 'categorical'
                else:
                    column_types[col] = 'text'
            else:
                column_types[col] = 'other'

        # Simple heuristics for potential targets
        for col in data.columns:
            if column_types.get(col) == 'numerical' and col.lower() in ['price', 'sales', 'revenue', 'score']:
                potential_targets.append(col)
            elif column_types.get(col) == 'categorical' and col.lower() in ['category', 'type', 'class']:
                potential_targets.append(col)

        key_insights.append(f"Dataset has {len(data.columns)} columns: {', '.join([f'{k} ({v})' for k,v in column_types.items()])}")
        if potential_targets:
            key_insights.append(f"Potential target columns: {', '.join(potential_targets)}")

        return {
            'column_types': column_types,
            'potential_targets': potential_targets,
            'key_insights': key_insights
        }
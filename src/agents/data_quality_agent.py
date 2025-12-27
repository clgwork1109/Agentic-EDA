import pandas as pd
from typing import Dict, Any

class DataQualityAgent:
    """
    Agent responsible for assessing data quality.
    Checks for missing values, duplicates, and basic anomalies.
    """

    def __init__(self):
        pass

    def process(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Assesses the quality of the dataset.

        Args:
            data (pd.DataFrame): The dataset.

        Returns:
            Dict[str, Any]: Structured output with quality metrics.
                - 'missing_values': dict of missing counts per column
                - 'duplicate_rows': int, number of duplicate rows
                - 'anomalies': dict of potential anomalies per column
                - 'quality_score': float, overall quality score (0-1)
        """
        missing_values = data.isnull().sum().to_dict()
        duplicate_rows = data.duplicated().sum()

        anomalies = {}
        for col in data.columns:
            if data[col].dtype in ['int64', 'float64']:
                # Simple anomaly: values beyond 3 std devs
                mean = data[col].mean()
                std = data[col].std()
                anomaly_count = ((data[col] - mean).abs() > 3 * std).sum()
                anomalies[col] = int(anomaly_count)
            else:
                anomalies[col] = 0  # For now, no anomalies for non-numerical

        # Simple quality score: based on missing and duplicates
        total_cells = data.shape[0] * data.shape[1]
        missing_cells = sum(missing_values.values())
        quality_score = 1 - (missing_cells / total_cells + duplicate_rows / data.shape[0])

        return {
            'missing_values': missing_values,
            'duplicate_rows': duplicate_rows,
            'anomalies': anomalies,
            'quality_score': max(0, min(1, quality_score))
        }
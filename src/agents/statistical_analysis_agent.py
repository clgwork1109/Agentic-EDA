import pandas as pd
from typing import Dict, Any
import numpy as np

class StatisticalAnalysisAgent:
    """
    Agent responsible for performing statistical analysis on the dataset.
    Computes summary statistics, correlations, and distributions.
    """

    def __init__(self):
        pass

    def process(self, data: pd.DataFrame, column_types: Dict[str, str]) -> Dict[str, Any]:
        """
        Performs statistical analysis on the dataset.

        Args:
            data (pd.DataFrame): The dataset.
            column_types (Dict[str, str]): Column classifications from SchemaSemanticsAgent.

        Returns:
            Dict[str, Any]: Structured output with statistical summaries.
                - 'numerical_stats': dict of summary stats for numerical columns
                - 'categorical_stats': dict of frequency stats for categorical columns
                - 'correlation_matrix': correlation matrix for numerical columns
                - 'outliers': dict of outlier counts per numerical column
        """
        numerical_stats = {}
        categorical_stats = {}
        correlation_matrix = None
        outliers = {}

        numerical_cols = [col for col, typ in column_types.items() if typ == 'numerical']
        categorical_cols = [col for col, typ in column_types.items() if typ == 'categorical']

        # Numerical stats
        if numerical_cols:
            desc = data[numerical_cols].describe()
            numerical_stats = desc.to_dict()
            # Correlation
            corr = data[numerical_cols].corr()
            correlation_matrix = corr.to_dict()
            # Outliers using IQR
            for col in numerical_cols:
                Q1 = data[col].quantile(0.25)
                Q3 = data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outlier_count = ((data[col] < lower_bound) | (data[col] > upper_bound)).sum()
                outliers[col] = int(outlier_count)

        # Categorical stats
        for col in categorical_cols:
            freq = data[col].value_counts().to_dict()
            categorical_stats[col] = freq

        return {
            'numerical_stats': numerical_stats,
            'categorical_stats': categorical_stats,
            'correlation_matrix': correlation_matrix,
            'outliers': outliers
        }
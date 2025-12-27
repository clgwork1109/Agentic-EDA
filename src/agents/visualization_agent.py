import pandas as pd
from typing import Dict, Any, List
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class VisualizationAgent:
    """
    Agent responsible for generating interactive visualizations for EDA.
    Creates charts for distributions, correlations, etc.
    """

    def __init__(self):
        pass

    def process(self, data: pd.DataFrame, column_types: Dict[str, str], stats: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates visualizations based on the dataset and statistics.

        Args:
            data (pd.DataFrame): The dataset.
            column_types (Dict[str, str]): Column types.
            stats (Dict[str, Any]): Statistical summaries.

        Returns:
            Dict[str, Any]: Structured output with Plotly figures.
                - 'histograms': list of histogram figures for numerical columns
                - 'boxplots': list of boxplot figures for numerical columns
                - 'bar_charts': list of bar charts for categorical columns
                - 'correlation_heatmap': correlation heatmap figure
        """
        visualizations = {
            'histograms': [],
            'boxplots': [],
            'bar_charts': [],
            'correlation_heatmap': None
        }

        numerical_cols = [col for col, typ in column_types.items() if typ == 'numerical']
        categorical_cols = [col for col, typ in column_types.items() if typ == 'categorical']

        # Histograms for numerical
        for col in numerical_cols[:5]:  # Limit to first 5 to avoid too many
            fig = px.histogram(data, x=col, title=f'Histogram of {col}')
            visualizations['histograms'].append(fig)

        # Boxplots for numerical
        for col in numerical_cols[:5]:
            fig = px.box(data, y=col, title=f'Boxplot of {col}')
            visualizations['boxplots'].append(fig)

        # Bar charts for categorical
        for col in categorical_cols[:5]:
            freq_df = data[col].value_counts().reset_index()
            freq_df.columns = ['category', 'count']
            fig = px.bar(freq_df, x='category', y='count', title=f'Frequency of {col}')
            visualizations['bar_charts'].append(fig)

        # Correlation heatmap
        if stats.get('correlation_matrix'):
            corr_df = pd.DataFrame(stats['correlation_matrix'])
            fig = px.imshow(corr_df, text_auto=True, title='Correlation Heatmap')
            visualizations['correlation_heatmap'] = fig

        return visualizations
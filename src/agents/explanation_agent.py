from typing import Dict, Any, List

class ExplanationAgent:
    """
    Agent responsible for generating plain-English explanations for all analyses.
    Provides what it shows, why it matters, and what to notice.
    """

    def __init__(self):
        # Could integrate LLM here, but for now, use templates
        pass

    def process(self, ingestion_output: Dict[str, Any], schema_output: Dict[str, Any],
                stats_output: Dict[str, Any], viz_output: Dict[str, Any], quality_output: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates explanations for all EDA components.

        Args:
            ingestion_output: From DatasetIngestionAgent
            schema_output: From SchemaSemanticsAgent
            stats_output: From StatisticalAnalysisAgent
            viz_output: From VisualizationAgent
            quality_output: From DataQualityAgent

        Returns:
            Dict[str, Any]: Explanations for each section.
        """
        explanations = {}

        # Dataset overview
        shape = ingestion_output['shape']
        explanations['dataset_overview'] = {
            'what': f"This dataset contains {shape[0]} rows and {shape[1]} columns.",
            'why': "Understanding the size helps assess the dataset's scope and potential for analysis.",
            'notice': f"With {shape[0]} records, the analysis should be reliable if representative."
        }

        # Schema
        col_types = schema_output['column_types']
        num_num = sum(1 for t in col_types.values() if t == 'numerical')
        num_cat = sum(1 for t in col_types.values() if t == 'categorical')
        explanations['schema'] = {
            'what': f"The dataset has {num_num} numerical and {num_cat} categorical columns.",
            'why': "Column types determine what analyses can be performed.",
            'notice': "Ensure categorical columns are properly encoded for modeling."
        }

        # Stats
        if stats_output['numerical_stats']:
            explanations['stats'] = {
                'what': "Summary statistics show mean, median, min, max for numerical columns.",
                'why': "These metrics reveal central tendencies and variability.",
                'notice': "Look for skewed distributions or unusual ranges."
            }

        # Quality
        qual_score = quality_output['quality_score']
        explanations['quality'] = {
            'what': f"Data quality score is {qual_score:.2f}, with {quality_output['duplicate_rows']} duplicates.",
            'why': "High quality data leads to reliable insights.",
            'notice': "Address missing values and duplicates before modeling."
        }

        # Visualizations
        explanations['visualizations'] = {
            'histograms': "Histograms show data distribution; look for normality or skewness.",
            'boxplots': "Boxplots highlight outliers and quartiles.",
            'correlation': "Heatmap shows relationships between variables."
        }

        return explanations
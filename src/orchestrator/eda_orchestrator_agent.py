from typing import Dict, Any
from ..agents.dataset_ingestion_agent import DatasetIngestionAgent
from ..agents.schema_semantics_agent import SchemaSemanticsAgent
from ..agents.statistical_analysis_agent import StatisticalAnalysisAgent
from ..agents.visualization_agent import VisualizationAgent
from ..agents.data_quality_agent import DataQualityAgent
from ..agents.explanation_agent import ExplanationAgent

class EDAOrchestratorAgent:
    """
    Orchestrator agent that coordinates all EDA agents.
    Manages the flow from data ingestion to final explanations.
    """

    def __init__(self):
        self.ingestion_agent = DatasetIngestionAgent()
        self.schema_agent = SchemaSemanticsAgent()
        self.stats_agent = StatisticalAnalysisAgent()
        self.viz_agent = VisualizationAgent()
        self.quality_agent = DataQualityAgent()
        self.explanation_agent = ExplanationAgent()

    def process(self, file_path: str) -> Dict[str, Any]:
        """
        Orchestrates the full EDA pipeline.

        Args:
            file_path (str): Path to the dataset file.

        Returns:
            Dict[str, Any]: Combined results from all agents.
        """
        # Step 1: Ingest data
        ingestion_result = self.ingestion_agent.process(file_path)
        data = ingestion_result['data']

        # Step 2: Analyze schema
        schema_result = self.schema_agent.process(data)

        # Step 3: Statistical analysis
        stats_result = self.stats_agent.process(data, schema_result['column_types'])

        # Step 4: Visualizations
        viz_result = self.viz_agent.process(data, schema_result['column_types'], stats_result)

        # Step 5: Data quality
        quality_result = self.quality_agent.process(data)

        # Step 6: Explanations
        explanation_result = self.explanation_agent.process(
            ingestion_result, schema_result, stats_result, viz_result, quality_result
        )

        return {
            'ingestion': ingestion_result,
            'schema': schema_result,
            'statistics': stats_result,
            'visualizations': viz_result,
            'quality': quality_result,
            'explanations': explanation_result
        }
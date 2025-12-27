# Explainable Agentic EDA Platform

An agent-based web application for comprehensive exploratory data analysis (EDA) with plain-English explanations.

## Features

- **Dataset Ingestion**: Support for CSV and Excel files with safe missing value handling
- **Schema Analysis**: Automatic classification of columns (numerical, categorical, datetime, text)
- **Statistical Analysis**: Summary statistics, correlations, and outlier detection
- **Interactive Visualizations**: Plotly-based charts for distributions and relationships
- **Data Quality Assessment**: Checks for missing values, duplicates, and anomalies
- **Explainable Insights**: Plain-English explanations for every analysis component

## Architecture

The platform uses a multi-agent system coordinated by an orchestrator:

- `DatasetIngestionAgent`: Handles file loading and preprocessing
- `SchemaSemanticsAgent`: Analyzes column types and semantics
- `StatisticalAnalysisAgent`: Computes statistical summaries
- `VisualizationAgent`: Generates interactive charts
- `DataQualityAgent`: Assesses data quality metrics
- `ExplanationAgent`: Provides human-readable explanations
- `EDAOrchestratorAgent`: Coordinates the entire pipeline

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Usage

1. Upload a CSV or Excel file via the sidebar
2. View dataset summary in the sidebar
3. Explore analysis results in the tabbed interface:
   - **Overview**: Dataset summary and sample data
   - **Column-wise Analysis**: Detailed stats and charts per column
   - **Correlations**: Relationship heatmap for numerical variables
   - **Data Quality**: Quality metrics and issues
   - **Insights**: Key findings and recommendations

## Technology Stack

- **Frontend**: Streamlit with custom dark theme
- **Backend**: Python with modular agent architecture
- **Data Handling**: Pandas
- **Visualization**: Plotly
- **File Support**: CSV, Excel (via openpyxl)

## Academic Context

This project demonstrates agent-based software architecture for data science applications, emphasizing explainability and modularity for educational and research purposes.
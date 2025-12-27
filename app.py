import streamlit as st
import pandas as pd
from src.orchestrator.eda_orchestrator_agent import EDAOrchestratorAgent
import tempfile
import os

# Set page config
st.set_page_config(
    page_title="Explainable Agentic EDA Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    .main {
        background-color: #2c2c2c;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #3c3c3c;
    }
    .stTabs [data-baseweb="tab-list"] {
        background-color: #3c3c3c;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #4c4c4c;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("📊 Explainable Agentic EDA Platform")
    st.markdown("Upload your dataset and let our agent system perform comprehensive exploratory data analysis.")

    # Sidebar
    with st.sidebar:
        st.header("Dataset Upload")
        uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx', 'xls'])

        if uploaded_file is not None:
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                file_path = tmp_file.name

            # Run orchestrator
            orchestrator = EDAOrchestratorAgent()
            results = orchestrator.process(file_path)

            # Display summary in sidebar
            st.subheader("Dataset Summary")
            st.write(f"Rows: {results['ingestion']['shape'][0]}")
            st.write(f"Columns: {results['ingestion']['shape'][1]}")
            st.write(f"Quality Score: {results['quality']['quality_score']:.2f}")

            # Clean up temp file
            os.unlink(file_path)

            # Main area with tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Column-wise Analysis", "Correlations", "Data Quality", "Insights"])

            with tab1:
                st.header("Dataset Overview")
                st.write(results['explanations']['dataset_overview']['what'])
                st.write("**Why it matters:**", results['explanations']['dataset_overview']['why'])
                st.write("**What to notice:**", results['explanations']['dataset_overview']['notice'])
                st.dataframe(results['ingestion']['data'].head())

            with tab2:
                st.header("Column-wise Analysis")
                col_types = results['schema']['column_types']
                for col, typ in col_types.items():
                    st.subheader(f"{col} ({typ})")
                    if typ == 'numerical':
                        st.write("Summary Stats:")
                        st.json(results['statistics']['numerical_stats'].get(col, {}))
                        # Show histogram if available
                        if results['visualizations']['histograms']:
                            for fig in results['visualizations']['histograms']:
                                if fig.data[0].x == col:
                                    st.plotly_chart(fig)
                                    break
                    elif typ == 'categorical':
                        st.write("Frequency:")
                        st.json(results['statistics']['categorical_stats'].get(col, {}))

            with tab3:
                st.header("Correlations")
                if results['visualizations']['correlation_heatmap']:
                    st.plotly_chart(results['visualizations']['correlation_heatmap'])
                else:
                    st.write("No numerical columns for correlation analysis.")

            with tab4:
                st.header("Data Quality")
                st.write(results['explanations']['quality']['what'])
                st.write("**Why it matters:**", results['explanations']['quality']['why'])
                st.write("**What to notice:**", results['explanations']['quality']['notice'])
                st.write("Missing Values:")
                st.json(results['quality']['missing_values'])
                st.write(f"Duplicate Rows: {results['quality']['duplicate_rows']}")

            with tab5:
                st.header("Insights")
                st.write("Key Insights from Schema Analysis:")
                for insight in results['schema']['key_insights']:
                    st.write(f"- {insight}")
                st.write("Potential Target Columns:", ", ".join(results['schema']['potential_targets']))

if __name__ == "__main__":
    main()
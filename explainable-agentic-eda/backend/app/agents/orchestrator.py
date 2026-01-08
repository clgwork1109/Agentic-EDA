from app.utils.file_loader import load_dataset

from app.agents.dataset_agent import analyze_dataset
from app.agents.quality_agent import assess_quality
from app.agents.planning_agent import plan_eda
from app.agents.stats_agent import statistical_summary
from app.agents.correlation_agent import correlation_matrix
from app.agents.insight_agent import detect_insights
from app.agents.explainability_agent import explain_sections

from app.pipelines.distributions import histogram_data
from app.pipelines.chart_builder import histogram_chart

def run_eda_pipeline(dataset_id: str):
    df = load_dataset(dataset_id)

    dataset_profile = analyze_dataset(df)
    quality = assess_quality(df)
    plan = plan_eda(dataset_profile)

    stats = statistical_summary(df)
    insights = detect_insights(stats)
    explanations = explain_sections(plan["sections"])

    charts = []

    for col in dataset_profile["numeric_columns"]:
        hist = histogram_data(df[col])
        charts.append(histogram_chart(col, hist))

    correlation = correlation_matrix(df)

    return {
        "status": "completed",

        "agents": {
            "dataset_understanding": dataset_profile,
            "data_quality": quality,
            "planning": plan,
            "statistics": stats,
            "insights": insights,
            "explainability": explanations
        },

        "charts": charts,
        "correlation": correlation
    }

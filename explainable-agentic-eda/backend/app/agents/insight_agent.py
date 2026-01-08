# Insight agent placeholder
def detect_insights(stats_summary):
    insights = []

    for col, stats in stats_summary.items():
        if abs(stats["skew"]) > 1:
            insights.append({
                "type": "distribution_skew",
                "column": col,
                "severity": "medium",
                "message": f"{col} shows high skewness ({stats['skew']:.2f})"
            })

        if stats["max"] > stats["mean"] * 3:
            insights.append({
                "type": "possible_outlier",
                "column": col,
                "severity": "high",
                "message": f"{col} may contain extreme outliers"
            })

    return insights

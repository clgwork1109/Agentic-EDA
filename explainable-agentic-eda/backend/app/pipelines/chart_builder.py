def histogram_chart(col_name, hist_data):
    return {
        "chart_type": "histogram",
        "echarts_option": {
            "xAxis": {
                "type": "category",
                "data": hist_data["labels"]
            },
            "yAxis": {
                "type": "value"
            },
            "series": [{
                "type": "bar",
                "data": hist_data["values"]
            }]
        },
        "title": f"Distribution of {col_name}"
    }

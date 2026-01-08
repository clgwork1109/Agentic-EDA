# Explainability agent placeholder
def explain_sections(sections):
    explanations = {}

    for section in sections:
        if section == "distributions":
            explanations[section] = "Distribution plots help understand data spread and skewness."
        elif section == "correlation":
            explanations[section] = "Correlation analysis highlights linear relationships between variables."
        elif section == "quality":
            explanations[section] = "Data quality checks identify missing values and duplicates."

    return explanations

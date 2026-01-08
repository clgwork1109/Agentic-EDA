# Planning agent placeholder
def plan_eda(dataset_profile):
    sections = ["kpis", "quality"]

    if len(dataset_profile["numeric_columns"]) > 1:
        sections.append("distributions")
        sections.append("correlation")

    return {
        "sections": sections
    }

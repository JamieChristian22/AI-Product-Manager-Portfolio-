# Generative AI Example – Pseudo Integration
def generate_kpi_summary(metrics):
    summary = f"""
    Weekly KPI Summary:
    Conversion: {metrics['conversion']}%
    Retention: {metrics['retention']}%
    Revenue: ${metrics['revenue']}
    """
    return summary

sample_metrics = {
    "conversion": 26,
    "retention": 48,
    "revenue": 125000
}

print(generate_kpi_summary(sample_metrics))

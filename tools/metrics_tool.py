import numpy as np

def analyze_metrics(metrics):
    insights = {}

    for k, v in metrics.items():
        if k == "day":
            continue

        trend = v[-1] - v[0]
        insights[k] = "declining" if trend < 0 else "improving"

    return insights
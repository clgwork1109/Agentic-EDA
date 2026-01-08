# Distributions pipeline placeholder
import numpy as np

def histogram_data(series, bins=10):
    counts, edges = np.histogram(series.dropna(), bins=bins)
    labels = [f"{round(edges[i],2)}–{round(edges[i+1],2)}" for i in range(len(counts))]

    return {
        "labels": labels,
        "values": counts.tolist()
    }

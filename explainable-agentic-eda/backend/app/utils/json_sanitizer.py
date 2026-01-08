import math

def sanitize_for_json(obj):
    """
    Recursively converts NaN / inf / -inf values to None
    so FastAPI can safely serialize the response.
    """
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj

    if isinstance(obj, dict):
        return {k: sanitize_for_json(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [sanitize_for_json(v) for v in obj]

    return obj

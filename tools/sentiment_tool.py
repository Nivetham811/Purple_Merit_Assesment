def sentiment_summary(feedback):
    negative = sum(1 for f in feedback if "bad" in f.lower() or "crash" in f.lower())
    positive = len(feedback) - negative

    return {
        "positive": positive,
        "negative": negative,
        "overall": "negative" if negative > positive else "positive"
    }
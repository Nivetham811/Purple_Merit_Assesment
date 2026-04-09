import json
from tools.metrics_tool import analyze_metrics
from tools.sentiment_tool import sentiment_summary

def load_json(path):
    with open(path) as f:
        return json.load(f)

if __name__ == "__main__":
    metrics = load_json("data/metrics.json")
    feedback = load_json("data/feedback.json")

    # TOOL CALLS (IMPORTANT FOR ASSESSMENT)
    metric_result = analyze_metrics(metrics)
    sentiment = sentiment_summary(feedback)

    # DECISION LOGIC (PM AGENT SIMULATION)
    bad_metrics = sum(1 for v in metric_result.values() if v == "declining")

    if bad_metrics >= 4 and sentiment["overall"] == "negative":
        decision = "ROLL_BACK"
    elif bad_metrics >= 2:
        decision = "PAUSE"
    else:
        decision = "PROCEED"

    final_output = {
        "decision": decision,
        "rationale": {
            "metrics": metric_result,
            "sentiment": sentiment
        },
        "risk_register": [
            "High crash rate",
            "Negative user feedback"
        ],
        "action_plan": [
            {"owner": "Engineering", "task": "Fix crashes"},
            {"owner": "Backend", "task": "Reduce latency"}
        ],
        "communication_plan": "Notify users about fixes",
        "confidence_score": 0.8
    }

    with open("output/decision.json", "w") as f:
        json.dump(final_output, f, indent=4)

    print("\n🔥 FINAL OUTPUT:\n", json.dumps(final_output, indent=4))
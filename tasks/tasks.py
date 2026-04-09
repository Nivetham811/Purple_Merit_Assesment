from crewai import Task
from tools.metrics_tool import analyze_metrics
from tools.sentiment_tool import sentiment_summary

def get_tasks(pm, data, marketing, risk, metrics, feedback):

    t1 = Task(
        description=f"Analyze metrics: {metrics}",
        agent=data,
        expected_output="Key metric trends and anomalies"
    )

    t2 = Task(
        description=f"Analyze user feedback: {feedback}",
        agent=marketing,
        expected_output="User sentiment summary"
    )

    t3 = Task(
        description="Identify risks based on metrics and sentiment",
        agent=risk,
        expected_output="List of risks"
    )

    t4 = Task(
        description="""
        Based on all inputs, decide:
        - Proceed / Pause / Rollback
        - Give reasoning
        - Provide action plan
        """,
        agent=pm,
        expected_output="Final decision with reasoning"
    )

    return [t1, t2, t3, t4]
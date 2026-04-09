from crewai import Agent

def get_agents():
    pm = Agent(
        role="Product Manager",
        goal="Decide go/no-go",
        backstory="Expert",
        llm=None
    )

    data = Agent(
        role="Data Analyst",
        goal="Analyze metrics",
        backstory="Expert",
        llm=None
    )

    marketing = Agent(
        role="Marketing",
        goal="Analyze feedback",
        backstory="Expert",
        llm=None
    )

    risk = Agent(
        role="Risk Analyst",
        goal="Find risks",
        backstory="Expert",
        llm=None
    )

    return pm, data, marketing, risk
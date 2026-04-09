# 🚀 AI Multi-Agent Release Decision System

## 📌 Overview

This project implements a **multi-agent AI system** using CrewAI to simulate real-world product decision-making after a feature release.

The system analyzes:

* 📊 Product metrics
* 💬 User feedback
* ⚠️ Risk signals

And produces a final decision:

👉 **ROLL_BACK** or **PROCEED**

---

## 🧠 Architecture

The system uses 4 specialized AI agents:

1. **Product Manager (PM)**

   * Makes final decision

2. **Data Analyst**

   * Analyzes metrics trends

3. **Marketing Analyst**

   * Evaluates user sentiment

4. **Risk Analyst**

   * Identifies risks and anomalies

---

## ⚙️ Tech Stack

* Python 3.10+
* CrewAI
* LangChain
---

## 📁 Project Structure

```
Crew/
│── main.py
│── config.py
│
├── agents/
│   └── agents.py
│
├── tasks/
│   └── tasks.py
│
├── tools/
│   └── tools.py
│
└── data/
    ├── metrics.json
    ├── feedback.json
    └── release_notes.txt
```

---

## 📊 Input Data

### 1. metrics.json

Contains time-series product metrics such as:

* conversion_rate
* dau (Daily Active Users)
* retention
* crash_rate
* latency
* payment_success

### 2. feedback.json

User feedback data used for sentiment analysis.

### 3. release_notes.txt (optional)

Describes the feature release.

---

## 🧪 How It Works

1. Data Analyst evaluates metrics trends 📉
2. Marketing Analyst analyzes user sentiment 💬
3. Risk Analyst identifies system risks ⚠️
4. Product Manager combines all insights

👉 Outputs final decision:

```json
{
  "decision": "ROLL_BACK",
  "reason": "High crash rate, declining conversion, negative feedback"
}
```

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install crewai langchain langchain-community
```

---
---

### 3. Run the Project

```bash
python main.py
```

---

## ❗ Important Notes

* This project runs **fully locally** (no API key required)
* Uses LLaMA 3 via Ollama instead of OpenAI
* Designed to simulate **real-world product failures**

---

## 🎯 Sample Outcome

If metrics degrade and feedback is negative:

👉 Output:

```
ROLL_BACK
```

---

## 🧠 Key Design Decisions

* Multi-agent architecture for modular reasoning
* Local LLM usage for cost efficiency
* Realistic failure simulation via synthetic data

---

## 💡 Future Improvements

* Add real-time streaming metrics
* Integrate dashboard visualization
* Use vector DB for historical analysis
* Add automated alerting system

---

## 👨‍💻 Author

AI/ML Engineer Assessment Submission

---

## ⭐ Conclusion

This system demonstrates how AI agents can collaboratively simulate **product decision-making pipelines**, similar to real-world tech companies.

---

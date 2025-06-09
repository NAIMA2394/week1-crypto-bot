# 🤖 naimacrypto - Rule-Based Chatbot for Cryptocurrency Advice

CryptoBuddy is a beginner-friendly Python chatbot that gives investment advice based on cryptocurrency **profitability** and **sustainability** using simple if-else logic.

## ✅ Features

- Answers queries like:
  - “Which crypto is trending up?”
  - “What’s the most sustainable coin?”
  - “Which crypto is best for long-term growth?”
- Uses a predefined dataset (Bitcoin, Ethereum, Cardano)
- Logic-based decision-making (no ML required!)

## 🛠️ Tech Stack

- Language: Python
- Platform: Run using Terminal or Jupyter Notebook
- Libraries: None required (uses built-in `input()` and `print()`)

## 📊 Crypto Dataset

```python
crypto_db = {
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3},
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6},
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8}
}

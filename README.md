# 🕵️‍♀️ AML Fraud Detection Engine

This project simulates an **Anti-Money Laundering (AML)** detection system that flags suspicious transactions using **customizable rule-based logic** in Python. Designed for fraud analysts, financial investigators, and machine learning engineers interested in risk detection, financial crime prevention, or regulatory technology (RegTech).

---

## 📂 Project Structure

```
aml-fraud-detection/
├── data/                     # Synthetic transaction dataset
│   └── synthetic_transactions.csv
├── config/                   # User-defined rules in JSON format
│   └── rules.json
├── scripts/                  # Python rule engine
│   └── apply_rules.py
├── outputs/                  # Generated output of flagged transactions
├── README.md                 # You're reading it!
```

---

## 🧠 How It Works

1. **Data Simulation**: Synthetic transactions with fields like amount, country, and type.
2. **Configurable Rules**: Define fraud flags like high-value transfers or risky geographies in a JSON file.
3. **Rule Engine**: Python script reads the rules and applies them to the dataset.
4. **Output**: Flags and saves suspicious transactions to `outputs/flagged_results.csv`.

---

## 📌 Sample Rules (`config/rules.json`)

```json
{
  "rules": {
    "flag_high_value": {
      "enabled": true,
      "column": "amount",
      "operator": "greater_than",
      "value": 10000
    },
    "flag_high_risk_country": {
      "enabled": true,
      "column": "location",
      "operator": "in",
      "value": ["CN", "RU"]
    }
  }
}
```

✅ **Users can add more rules** using operators:
- `greater_than`
- `less_than`
- `in`
- `not_in`

---

## 🛠️ To Run

### Prerequisites
- Python 3.x
- pandas

### Step-by-Step

1. Clone the repo:
```bash
git clone https://github.com/bhumagain999/aml-fraud-detection.git
```

2. Run the rule engine:
```bash
cd aml-fraud-detection/scripts
python apply_rules.py
```

3. View results in:
```
outputs/flagged_results.csv
```

---

## 📊 Sample Output

| transaction_id | amount | location | suspicious |
|----------------|--------|----------|------------|
| TXN1           | 12000  | CN       | ✅         |
| TXN3           | 30000  | RU       | ✅         |

---

## 🚀 Future Enhancements

- ✅ Add Streamlit dashboard
- 📈 Integrate real transaction datasets (with anonymization)
- 🤖 Add unsupervised learning (e.g., Isolation Forest, Autoencoders)
- 🧩 Blockchain integration for crypto tracing

---

## 📧 Contact

Built by [Bijaya Humagain](https://github.com/bhumagain999) — feel free to contribute or fork!

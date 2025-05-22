
# 🕵️ AML Fraud Detection Engine

This project simulates a real-world **Anti-Money Laundering (AML)** detection system. It flags suspicious financial transactions based on configurable rules, applies them to datasets like **Kaggle's credit card fraud dataset**, and visualizes the output via an interactive Streamlit dashboard.

---

## 📦 Features

- ✅ Rule-based fraud detection using `rules.json`
- ✅ Compatible with both synthetic and real datasets (`creditcard.csv`)
- ✅ Modular and extensible Python scripts
- ✅ Interactive Streamlit dashboards to explore flagged results
- ✅ Clean GitHub structure and easy to deploy

---

## 🧠 How It Works

1. Load transactions from `data/creditcard.csv`
2. Read configurable detection rules from `config/rules.json`
3. Run `scripts/apply_rules.py` to flag suspicious activity
4. Output results to `outputs/flagged_creditcard_results.csv`
5. Explore results using `streamlit_app/dashboard_creditcard.py`

---

## 🛠 Requirements

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### Apply Rules

```bash
python scripts/apply_rules.py
```

### Launch Streamlit Dashboard

```bash
cd streamlit_app
streamlit run dashboard_creditcard.py
```

---

## 📁 Folder Structure

```
aml-fraud-detection/
├── data/                 # Datasets (creditcard.csv, synthetic_transactions.csv)
├── config/               # JSON-based rule configuration
├── scripts/              # Python rule engine
├── outputs/              # Flagged results
├── streamlit_app/        # Interactive dashboards
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 📊 Dashboard Preview

Explore rule flag counts, transaction amounts, fraud time trends, and PCA component anomalies interactively in Streamlit.

---

## 📚 Credits

- Dataset: [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Libraries: `pandas`, `numpy`, `streamlit`, `matplotlib`, `seaborn`

---

## 💡 Ideas for Expansion

- Add ML-based scoring alongside rule engine
- Create Streamlit controls for real-time threshold tweaking
- Build a user-friendly rule-builder UI

---

## 👤 Author

**Bijaya Humagain**  
[github.com/bhumagain999](https://github.com/bhumagain999)

---



# 🧾 Streamlit Dashboard – Credit Card Fraud Detection

This dashboard is a part of the **AML Fraud Detection** project and is built using **Streamlit** to explore, analyze, and visualize suspicious transactions flagged by rule-based detection logic applied to the Kaggle credit card fraud dataset.

---

## 📊 Features

- Visual summary of rule-based flags (high value, early time, negative V1)
- Comparison of suspicious vs normal transaction amounts
- Time-based fraud pattern visualization
- Anomaly detection using PCA component (V1)
- Interactive dashboard deployed using Streamlit

---

## 🚀 Run Locally

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Run the App

```bash
cd streamlit_app
streamlit run dashboard_creditcard.py
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repository to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Create a new app and select the following script:

```
streamlit_app/dashboard_creditcard.py
```

4. Connect your GitHub repo and click **Deploy**

---

## 📁 Folder Structure

```
aml-fraud-detection/
├── data/
│   └── creditcard.csv
├── config/
│   └── rules.json
├── scripts/
│   └── apply_rules.py
├── outputs/
│   └── flagged_creditcard_results.csv
├── streamlit_app/
│   └── dashboard_creditcard.py
│   └── README.md ← This file
```

---

## 🙌 Credits

- Dataset: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Built with: `streamlit`, `pandas`, `matplotlib`, `seaborn`

---

## 💡 Next Steps

- Add user-defined threshold controls (e.g., slider for amount)
- Integrate with ML model predictions
- Deploy both synthetic and real-data dashboards in one app

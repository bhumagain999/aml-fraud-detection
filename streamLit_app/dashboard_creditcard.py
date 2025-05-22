
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Credit Card Fraud Detection Insights", layout="wide")

# Set file path
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
flagged_path = os.path.join(base_path, "outputs", "flagged_creditcard_results.csv")

# Load data
df = pd.read_csv(flagged_path)
st.title("🔍 Credit Card Fraud Detection Dashboard")
st.markdown("This dashboard explores flagged transactions based on custom rule logic applied to the Kaggle credit card dataset.")

# Rule summary
rule_flags = [col for col in df.columns if col.startswith("flag_")]
st.subheader("✅ Rule Flag Summary")
flag_counts = df[rule_flags + ["suspicious"]].sum().astype(int)
st.bar_chart(flag_counts)

# Amount distribution
st.subheader("💰 Amount Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(df[df["suspicious"] == True]["Amount"], bins=40, color="red", label="Suspicious", ax=ax1, kde=True)
sns.histplot(df[df["suspicious"] == False]["Amount"], bins=40, color="green", label="Normal", ax=ax1, kde=True)
ax1.legend()
ax1.set_xlabel("Transaction Amount")
ax1.set_title("Suspicious vs Normal Amount Distribution")
st.pyplot(fig1)

# Time-based visualization
st.subheader("🕒 Time vs Suspicious Transactions")
fig2, ax2 = plt.subplots()
sns.histplot(data=df, x="Time", hue="suspicious", bins=50, multiple="stack", ax=ax2)
ax2.set_title("Transactions by Time")
st.pyplot(fig2)

# V1 anomaly view
if "V1" in df.columns:
    st.subheader("📉 V1 Anomaly Detection")
    fig3, ax3 = plt.subplots()
    sns.kdeplot(df[df["suspicious"] == True]["V1"], color="red", label="Suspicious", fill=True, ax=ax3)
    sns.kdeplot(df[df["suspicious"] == False]["V1"], color="blue", label="Normal", fill=True, ax=ax3)
    ax3.legend()
    ax3.set_title("Distribution of V1 Feature")
    st.pyplot(fig3)

# Conclusion
st.subheader("🧠 Observations & Insights")
st.markdown("""
- **High-value transactions** dominate among suspicious records (especially > $1000).
- **Early transactions** (Time < 10,000 seconds) show unusual frequency in flagged results.
- **V1 component** shows significant deviation between normal and suspicious sets, indicating a strong signal.
- Rules can be enhanced by tuning thresholds or incorporating more PCA components.
""")

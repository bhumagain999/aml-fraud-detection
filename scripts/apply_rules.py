
import pandas as pd
import json
import os

# Set paths
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path_synthetic = os.path.join(base_path, "data", "synthetic_transactions.csv")
data_path_credit = os.path.join(base_path, "data", "creditcard.csv")
rules_path = os.path.join(base_path, "config", "rules.json")

# Load rules
with open(rules_path, "r") as f:
    config = json.load(f)
rules = config.get("rules", {})

# Load the credit card dataset if available, else use synthetic
if os.path.exists(data_path_credit):
    print("🔄 Using creditcard.csv dataset")
    df = pd.read_csv(data_path_credit)
    output_file = "flagged_creditcard_results.csv"
else:
    print("🔄 Using synthetic_transactions.csv dataset")
    df = pd.read_csv(data_path_synthetic)
    output_file = "flagged_results.csv"

# Apply rules
for rule_name, rule in rules.items():
    if rule.get("enabled", False):
        col = rule["column"]
        op = rule["operator"]
        val = rule["value"]
        if col in df.columns:
            if op == "greater_than":
                df[rule_name] = df[col] > val
            elif op == "less_than":
                df[rule_name] = df[col] < val
            elif op == "in":
                df[rule_name] = df[col].isin(val)
            elif op == "not_in":
                df[rule_name] = ~df[col].isin(val)
        else:
            print(f"⚠️ Column '{col}' not found in dataset. Skipping rule '{rule_name}'.")

# Combine flags
rule_flags = [col for col in df.columns if col.startswith("flag_")]
df["suspicious"] = df[rule_flags].any(axis=1)

# Save results
output_path = os.path.join(base_path, "outputs", output_file)
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"✅ Flagged results saved to: {output_path}")

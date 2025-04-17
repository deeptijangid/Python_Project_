import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("C:\\Users\\najan\\Downloads\\Lobbyist_Agent_Employers_20250306.csv")

# Clean column names
df.columns = df.columns.str.strip()


# --- 1. Top 10 Most Active Lobbyist Agents ---
x = df['agent_name'].value_counts().nlargest(10).index
y = df['agent_name'].value_counts().nlargest(10).values

colors = ["lightseagreen", "lightyellow", "thistle", "lightskyblue", "sandybrown", "yellowgreen", "lightgray", "plum", "honeydew", "khaki"]
plt.figure(figsize=(12, 6), facecolor='aliceblue')
plt.bar(x, y, color=colors, edgecolor='black')
plt.title("Top 10 Most Active Lobbyist Agents")
plt.ylabel("Employer Connections")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

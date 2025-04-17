# --- 2. Most Common Employer Registration Titles ---
regt = df['employment_registration_title'].value_counts().nlargest(10)
x = regt.index
y = regt.values
plt.figure(figsize=(12, 6), facecolor='oldlace')
colors = ["lightblue", "steelblue", "lightgreen", "lightpink", "red", "sandybrown", "plum", "purple", "khaki", "chocolate"]
plt.bar(x, y, color=colors, edgecolor='black')
plt.title("Top 10 Employer Registration Titles")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

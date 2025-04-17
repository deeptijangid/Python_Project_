# --- 4. Number of Unique Employers per Lobbyist ---
unique_counts = df.groupby('agent_name')['employer_id'].nunique()

plt.figure(figsize=(12, 6))
colors = plt.cm.plasma(np.linspace(0.2, 0.9, 20))
bars = plt.hist(unique_counts, bins=20, edgecolor='black', alpha=0.95)[2]

for bar, color in zip(bars, colors):
    bar.set_facecolor(color)

plt.title("Unique Employers per Lobbyist")
plt.xlabel("Number of Unique Employers")
plt.ylabel("Number of Lobbyists")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

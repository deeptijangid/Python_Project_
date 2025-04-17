# --- 3. Registrations Over the Years ---
df['cleaned_year'] = pd.to_numeric(df['employment_year'].str.replace(",", ""), errors='coerce')
reg = df['cleaned_year'].value_counts().sort_index()
x = reg.index
y = reg.values
plt.figure(figsize=(12, 6))
plt.plot(x, y, marker='o', linestyle='-', color='purple', linewidth=2)
plt.title("Lobbyist Registrations Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Registrations")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

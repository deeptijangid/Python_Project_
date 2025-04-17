# --- 5. Employment Year vs Unique Employers per Agent ---
a = df.groupby(['agent_name', 'cleaned_year'])['employer_id'].nunique().reset_index()
a.columns = ['agent_name', 'year', 'unique_employer_count']
x=a['year']
y=a['unique_employer_count']
plt.figure(figsize=(12, 6))
plt.scatter(x,y,c=a['unique_employer_count'],cmap='plasma',edgecolors='black',alpha=0.7)
plt.title("Employment Year vs. Unique Employers per Agent")
plt.xlabel("Employment Year")
plt.ylabel("Unique Employers")
plt.colorbar(label="Unique Employers")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

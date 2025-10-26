# visualization_bar.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Read CSV
df = pd.read_csv("dominant_genres_per_decade.csv")

# 2) Defensive cleaning: drop Unknown decades if present
df = df[df['decade'] != "Unknown"]

# 3) Count decades dominated per genre
genre_counts = df['tag_name'].value_counts().reset_index()
genre_counts.columns = ['tag_name', 'decades_dominated']
# sort ascending so largest appear at top when using barh (tail -> biggest)
genre_counts = genre_counts.sort_values('decades_dominated', ascending=True)

# 4) (Optional) focus on top N genres
# top_n = 12
# genre_counts = genre_counts.tail(top_n)

# 5) Plot
sns.set_style("whitegrid")
plt.rcParams.update({"font.size": 10})
fig, ax = plt.subplots(figsize=(10, 6))

y = genre_counts['tag_name']
x = genre_counts['decades_dominated']

# Use a categorical colormap sized to number of genres
colors = sns.color_palette("tab10", n_colors=len(genre_counts))
ax.barh(y, x, color=colors)

ax.set_xlabel("Number of decades dominated")
ax.set_title("Top Genres by Number of Decades Dominated")

# 6) Annotate numeric counts on bars
for i, v in enumerate(x):
    ax.text(v + 0.1, i, str(v), va='center', fontsize=9)

plt.tight_layout()
# 7) Save
plt.savefig("timeline_bbar_chart.png", dpi=300, bbox_inches='tight')
plt.savefig("timeline_bbar_chart.svg", bbox_inches='tight')
plt.show()

# visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

def read_and_prepare(path="dominant_genres_per_decade.csv"):
    # 1) Read the CSV
    df = pd.read_csv(path)

    # 2) Ensure decade_num is numeric and drop rows without it (Unknown already excluded if you followed earlier steps)
    df['decade_num'] = pd.to_numeric(df['decade_num'], errors='coerce')

    # 3) If examples column is a stringified list, parse it to a Python list for possible annotations
    def parse_examples(cell):
        if pd.isna(cell):
            return []
        if isinstance(cell, list):
            return cell
        if isinstance(cell, str):
            cell = cell.strip()
            # try ast.literal_eval on strings that look like lists
            if cell.startswith('[') and cell.endswith(']'):
                try:
                    return ast.literal_eval(cell)
                except Exception:
                    return [cell]
            else:
                return [cell]
        return []

    if 'examples' in df.columns:
        df['examples_parsed'] = df['examples'].apply(parse_examples)
    else:
        df['examples_parsed'] = [[] for _ in range(len(df))]

    # 4) Sort chronologically
    df = df.sort_values('decade_num').reset_index(drop=True)

    return df

def plot_timeline(df, out_file="dominant_genres_timeline.png", annotate_top_n=6):
    """
    df: DataFrame with columns: decade, tag_name, books_count, decade_num, examples_parsed
    annotate_top_n: annotate this many largest points (by books_count) to avoid clutter
    """
    # --- Choose a sensible ordering of genres on the y-axis ---
    # We order genres by how many decades they dominated (desc). This brings most important genres to top.
    genre_order = df['tag_name'].value_counts().index.tolist()
    # Create a categorical y value mapping
    y_map = {g: i for i, g in enumerate(genre_order)}

    # --- Begin plot ---
    plt.figure(figsize=(14, 7))
    sns.set_style("whitegrid")  # seaborn style; optional

    # Scatter: x = decade_num, y = categorical (mapped), size = books_count
    sizes = df['books_count'].values
    # scale sizes so they look reasonable on the plot
    size_min, size_max = 80, 1200
    # linear scaling from observed counts to [size_min, size_max]
    if sizes.max() == sizes.min():
        s_scaled = [ (size_min + size_max) / 2 ] * len(sizes)
    else:
        s_scaled = ((sizes - sizes.min()) / (sizes.max() - sizes.min())) * (size_max - size_min) + size_min

    # plot points
    plt.scatter(df['decade_num'], df['tag_name'].map(y_map), s=s_scaled, alpha=0.8)

    # Y-axis: label ticks with genre names in the order chosen
    yticks = list(y_map.values())
    ylabels = list(y_map.keys())
    plt.yticks(yticks, ylabels)

    # X-axis: show decades as integers
    xticks = sorted(df['decade_num'].unique())
    plt.xticks(xticks, [f"{int(x)}s" for x in xticks], rotation=45)

    plt.xlabel("Decade")
    plt.title("Dominant Genre per Decade — timeline (dot size ∝ books_count)")
    plt.ylabel("Genre")

    # Add a legend-like size table (manually)
    # pick 3 representative sizes (small, medium, large)
    rep_counts = [int(df['books_count'].min()), int(df['books_count'].median()), int(df['books_count'].max())]
    rep_sizes = [ ((c - sizes.min()) / (sizes.max() - sizes.min())) * (size_max - size_min) + size_min if sizes.max()!=sizes.min() else (size_min+size_max)/2 for c in rep_counts ]
    for i, (rc, rs) in enumerate(zip(rep_counts, rep_sizes)):
        plt.scatter([], [], s=rs, label=f"{rc} books")
    plt.legend(scatterpoints=1, frameon=True, title="books_count (examples)")

    # Annotate only the largest N points to keep the plot readable
    df_sorted = df.sort_values('books_count', ascending=False).head(annotate_top_n)
    for _, row in df_sorted.iterrows():
        x = row['decade_num']
        y = y_map[row['tag_name']]
        # example text: first example if available
        ex = row['examples_parsed']
        label = ex[0] if len(ex) > 0 else ""
        # keep labels short (truncate)
        if len(label) > 60:
            label = label[:57] + "..."
        plt.text(x + 1.5, y + 0.05, label, fontsize=8, alpha=0.9)  # offset right a bit

    plt.tight_layout()
    plt.savefig(out_file, dpi=300)
#    plt.show()
    plt.savefig("timeline_bubble_chart.png", dpi=300, bbox_inches="tight")
if __name__ == "__main__":
    df = read_and_prepare("dominant_genres_per_decade.csv")
    print("Loaded rows:", len(df))
    print("Genres in this dataset:", df['tag_name'].unique())
    plot_timeline(df)

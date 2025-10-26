import pandas as pd
import numpy as np

def year_to_decade(y):
    if pd.isna(y):
        return "Unknown"
    y = int(y)
    if y < 1800 or y > 2025:
        return "Unknown"
    decade = (y // 10) * 10
    return f"{decade}s"

tag_mapping = {
    # Fiction categories
    "adult": "fiction",
    "adult-fiction": "fiction",
    "general-fiction": "fiction",
    "contemporary": "fiction",
    "contemporary-fiction": "fiction",
    "realistic-fiction": "fiction",
    "literary-fiction": "fiction",
    "modern-fiction": "fiction",
    "historical": "historical-fiction",
    "speculative-fiction": "science-fiction",  # or keep separate if you prefer

    # YA / Children
    "ya": "young-adult",
    "ya-fiction": "young-adult",
    "ya-books": "young-adult",
    "ya-fantasy": "young-adult",
    "young-adult-fiction": "young-adult",
    "youth": "young-adult",
    "school": "young-adult",
    "high-school": "young-adult",
    "coming-of-age": "young-adult",
    "young-adults": "young-adult",

    "childhood": "children",
    "childrens": "children",
    "children-s": "children",
    "children-s-books": "children",
    "childrens-books": "children",
    "kids": "children",
    "kids-books": "children",
    "juvenile": "children",

    # Sci-Fi / Fantasy
    "sci-fi": "science-fiction",
    "scifi": "science-fiction",
    "scifi-fantasy": "science-fiction",
    "sci-fi-fantasy": "science-fiction",
    "fantasy-sci-fi": "science-fiction",
    "fantasy-scifi": "science-fiction",
    "science-fiction-fantasy": "science-fiction",

    "urban-fantasy": "fantasy",
    "magic": "fantasy",

    # Crime / Mystery / Thriller
    "crime": "crime-fiction",
    "mystery-crime": "crime-fiction",
    "crime-mystery": "crime-fiction",
    "detective": "crime-fiction",

    "mystery-thriller": "mystery",
    "mystery-suspense": "mystery",
    "mysteries": "mystery",

    "thrillers": "thriller",
    "suspense-thriller": "thriller",

    # Horror / Paranormal
    "paranormal": "horror",
    "supernatural": "horror",

    # Comedy
    "humor": "comedy",
    "humour": "comedy",
    "funny": "comedy",

    # Other mappings
    "action": "adventure",
    "action-adventure": "adventure",
    "family": "drama",
    "friendship": "drama",
    "relationships": "drama",
    "love": "romance",

    "nonfiction": "non-fiction",
    "non-fiction": "non-fiction"
}

valid_tags = {
"fantasy", "science-fiction", "mystery", "romance", "historical-fiction", "non-fiction", "biography", "poetry", "horror", "thriller", "young-adult", "children", "philosophy", "history", "adventure", "drama", "science",
}

books = pd.read_csv("books.csv", usecols=["goodreads_book_id", "title", "authors", "original_publication_year"])

book_tags = pd.read_csv("book_tags.csv")
tags = pd.read_csv("tags.csv")

bt = book_tags.merge(tags, on="tag_id", how="left")

bt_books = bt.merge(books, on="goodreads_book_id", how="left")

bt_books['year'] = pd.to_numeric(bt_books['original_publication_year'], errors='coerce')
bt_books['decade'] = bt_books['year'].apply(year_to_decade)
bt_books['tag_name'] = bt_books['tag_name'].str.lower()
bt_books['tag_name'] = bt_books['tag_name'].replace(tag_mapping)
bt_books = bt_books[bt_books['tag_name'].isin(valid_tags)]


idx = bt_books.groupby('goodreads_book_id')['count'].idxmax()
primary = bt_books.loc[idx, ['goodreads_book_id','title','authors','year','decade','tag_id','tag_name','count']]
primary_known = primary[primary['decade'] != "Unknown"].copy()

decade_genre_counts = (
    primary_known
    .groupby(['decade','tag_name'])
    .size()
    .reset_index(name='books_count')
    .sort_values(['decade','books_count'], ascending=[True,False])
)



idx = decade_genre_counts.groupby('decade')['books_count'].idxmax()
dominant_by_decade = decade_genre_counts.loc[idx].copy()
dominant_by_decade['decade_num'] = dominant_by_decade['decade'].str.extract(r'(\d+)').astype(float)
dominant_by_decade = dominant_by_decade.sort_values('decade_num')

unknown_count = primary[primary['decade'] == "Unknown"].shape[0]

book_with_tags = bt_books.groupby('goodreads_book_id')['tag_name'].apply(list).reset_index()

tag_counts = bt_books['tag_name'].value_counts().reset_index()
tag_counts.columns = ['tag_name', 'count']

# Add sample titles for each dominant genre per decade
samples = []

for _, row in dominant_by_decade.iterrows():
    decade = row["decade"]
    genre = row["tag_name"]

    # get numeric decade range (e.g., 1980–1989)
    if pd.notna(row["decade_num"]):
        start = int(row["decade_num"])
        end = start + 9

        # filter primary books for this decade + genre
        subset = primary_known[
            (primary_known["year"].between(start, end)) &
            (primary_known["tag_name"] == genre)
        ]

        # pick up to 2 titles
        sample_titles = subset["title"].head(2).tolist()

        samples.append(sample_titles)
    else:
        samples.append([])

# Add the samples column to the dataframe
dominant_by_decade["examples"] = samples

dominant_by_decade.to_csv("dominant_genres_per_decade.csv", index=False)


#print("books", books.shape)
#print("book_tags", book_tags.shape)
#print("tags:", tags.shape)
#print("missing tag_name:", bt['tag_name'].isna().sum())
#print("merged bt_books shape:", bt_books.shape)
#print("rows with missing book info:", bt_books['title'].isna().sum())
#print(bt_books[['year','decade']].drop_duplicates().sort_values('year').head(10))
#print("Count per decade:", bt_books['decade'].value_counts().head(15))
#print("primary sample:", primary.head())
#print(bt_books[['title','year','decade']].sample(10))
#print("Dominant genre per decade:")
#print(dominant_by_decade)
#print(f"Books with Unknown decade: {unknown_count}")
#print(bt_books['tag_name'].sample(20))
#print(book_with_tags.head(5))
#print(tag_counts.head(200))
#print("Unexpected tags:", set(bt_books['tag_name'].unique()) - valid_tags)
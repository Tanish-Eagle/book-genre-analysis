# Charting Literary Power: Genre Dominance Across the Centuries

## Overview

This project explores the rise and fall of literary genres across two centuries — from the 1800s to the 2010s — based on data derived from the **Goodbooks-10k** dataset (a public dataset available on Kaggle).

I used Python for data cleaning, transformation, and visualization, ultimately producing both a **line plot** showing genre trends over time and a **bar plot** summarizing overall dominance across decades.

---

## Objectives

- To identify which genres dominated in each decade between 1800s and 2010s.

- To observe long-term shifts in literary trends, from poetry and romance in early decades to fantasy and non-fiction in modern times.

- To demonstrate a complete data analysis workflow — from raw data to tidy format and visual interpretation.

---

## Process Summary

1. **Data Acquisition:** I used the publicly available *Goodbooks-10k* dataset from Kaggle, which contains metadata for 10,000 books and approximately six million Goodreads ratings.

2. **Data Cleaning and Preparation:**
  - Removed irrelevant tags (such as *to-read*, *audiobook*, *ebook*, and numeric tags).
  - Grouped books by decade of publication.  
  - Identified the dominant genre in each decade, along with two sample titles from that genre.  
  - Exported the resulting tidy data to a CSV file (`dominant_genres_per_decade.csv`).

3. **Visualization:**  
  - **Line Plot:** Displaying the temporal progression of dominant genres across decades.  
  - **Bar Plot:** Showing the count of decades each genre dominated, providing a summary perspective of genre influence over time.

---

## Visualizations

1. **Line Plot — Temporal Genre Dominance** Illustrates the rise and decline of various genres from 1800s to 2010s.

2. **Bar Plot — Overall Genre Dominance** Shows which genres dominated the most decades overall.  
   Historical fiction and fantasy emerged as the most recurrent genres over the two centuries.

---

## Report

The detailed report titled  
**_“Charting Literary Power: Genre Dominance Across the Centuries”_**  
is included in this repository. It presents the methodology, interpretation of results, and reflections on the observed literary trends.

---

## Licensing

- **Code:** MIT License  

You are free to reuse or adapt this project with appropriate credit.

---

## Acknowledgments

- Dataset: [Goodbooks-10k Dataset on Kaggle](https://www.kaggle.com/zygmunt/goodbooks-10k)
- Tools used: Python, Pandas, NumPy, Matplotlib  

---

## Author

**Tanish Shrivastava:** A data enthusiast exploring how storytelling patterns evolve through the centuries.

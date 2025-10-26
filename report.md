This project was created for an academic assignment analyzing literary genre trends across decades. The analysis and interpretations are my own.

# Charting Literary Power: Genre Dominance Across the Centuries

## Executive Summary

This report examines the historical trajectory of literary genres from the early nineteenth century to the early twenty-first century. Using the goodbooks-10k dataset, which comprises 10,000 books and approximately six million ratings from Goodreads, the analysis identifies the prevailing genres across decades and explores the cultural or historical contexts that shaped their dominance. Through data cleaning and transformation with Python (Pandas and NumPy), dominant genres were extracted by decade and visualized using line and bar plots. The findings highlight not only the cyclical return of certain genres—such as romance and nonfiction—but also the emergence of new literary forms in response to societal shifts, including the rise of science fiction during the space race and fantasy during the late twentieth century. The report demonstrates how literature both reflects and responds to historical change, offering insights into the cultural preoccupations of different eras.

## Introduction

Books, much like other forms of media, are organized into genres. Yet unlike modern entertainment, literature is among the oldest mediums of knowledge transmission, serving dual purposes: to entertain and to educate.

Motivated by a personal interest in books, I undertook an analysis of literary genres across decades, aiming to chart their rise, decline, and resurgence, as well as to identify the decades in which specific genres achieved dominance. This document presents the results of that analysis.

## Data Acquisition and Preparation

For this assignment, I initially considered datasets containing publication metadata but found them unsuitable for the intended analysis. I subsequently selected the [goodbooks-10k dataset from Kaggle,](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k) which includes information about 10,000 books and six million Goodreads ratings.

To prepare the dataset, I employed Python with Pandas and NumPy. CSV files containing book titles, publication years, and Goodreads tags (genres) were imported. Non-informative or redundant tags (e.g., “ebook,” “to-read,” “audiobook”) as well as numerically coded tags were filtered out. From the cleaned data, I identified the dominant genres for each decade, counted the number of books per genre, and selected representative examples from each period.

## Findings

The analysis begins with the 1800s. In that decade, nonfiction dominated, followed by romance and poetry. From the 1830s through the 1880s, historical fiction prevailed. Representative works include War and Peace and The Adventures of Huckleberry Finn. It is worth noting, however, that such works may not have been originally classified as “historical fiction”; this label was often retrospectively applied by later readers and critics.

In the 1890s, horror emerged as the dominant genre—unsurprising given the publication of Bram Stoker’s Dracula, a novel that continues to influence the genre over a century later. Historical fiction regained prominence in the 1920s and 1930s, followed by children’s literature in the 1940s, perhaps reflecting a post-war desire to inspire optimism.

Science fiction rose to dominance in the 1950s, paralleling the early space race and advances in computing, with authors such as Isaac Asimov and Robert Heinlein gaining recognition. Children’s literature dominated the 1960s, while nonfiction re-emerged in the 1970s, reflecting the era’s interest in political and journalistic accounts.

From the 1980s to the 2000s, fantasy held sway, with Harry Potter and related works defining an era. Finally, romance reasserted dominance in the 2010s, returning to prominence after two centuries.

## Visualizations

Two visualizations were employed:

1. Line Plot (Temporal Trends): This chart traces the rise and fall of genres from the 1800s through the 2010s. It reveals an overall increase in the number of published works, especially after the 1910s. Despite the emergence of competing media—radio, television, the internet, video games—literary production remained robust.

2. Bar Plot (Genre Dominance Totals): This chart aggregates dominant genres across the two centuries. Historical fiction ranks first, likely reflecting retrospective categorization. Fantasy follows, then children’s literature and nonfiction (tied). Other genres achieved dominance in isolated decades without regaining prominence.


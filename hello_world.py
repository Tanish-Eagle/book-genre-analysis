import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Test pandas + numpy
data = {
    "decade": ["1980s", "1990s", "2000s", "2010s"],
    "books_count": [120, 340, 560, 420]
}
df = pd.DataFrame(data)

print("DataFrame preview:")
print(df)

# Test matplotlib
plt.plot(df["decade"], df["books_count"], marker="o")
plt.title("Hello World Plot")
plt.xlabel("Decade")
plt.ylabel("Books Count")
plt.show()

# Test seaborn (optional, but nicer style)
sns.barplot(x="decade", y="books_count", data=df)
plt.title("Hello World Bar Chart")
plt.show()

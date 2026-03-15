import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../data/cleaned/EV_population_cleaned.csv")

# Count EVs by company
brand_counts = df["Make"].value_counts().head(10)

print(brand_counts)

# Plot bar chart
plt.figure()

brand_counts.plot(kind="bar")

plt.title("Top 10 EV Brands")
plt.xlabel("Brand")
plt.ylabel("Number of Vehicles")

plt.xticks(rotation=45)

plt.grid(True)

# Save chart
plt.savefig("../outputs/charts/top_ev_brands.png")

# Show chart
plt.show()
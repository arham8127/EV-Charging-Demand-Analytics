import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../data/cleaned/EV_population_cleaned.csv")

# Count EVs by Model Year
ev_year = df["Model Year"].value_counts().sort_index()

print(ev_year)

# Plot chart
plt.figure()
ev_year.plot(kind="line")

plt.title("EV Growth Trend by Year")
plt.xlabel("Year")
plt.ylabel("Number of EV Vehicles")

plt.grid(True)

# Save chart
plt.savefig("../outputs/charts/EV_growth_trend.png")

# Show chart
plt.show()
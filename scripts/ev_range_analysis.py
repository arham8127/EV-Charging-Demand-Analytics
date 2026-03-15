import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../data/cleaned/EV_population_cleaned.csv")

# Plot histogram of electric range
plt.figure()

plt.hist(df["Electric Range"], bins=20)

plt.title("Electric Vehicle Range Distribution")
plt.xlabel("Electric Range (km)")
plt.ylabel("Number of Vehicles")

plt.grid(True)

# Save chart
plt.savefig("../outputs/charts/ev_range_distribution.png")

# Show chart
plt.show()
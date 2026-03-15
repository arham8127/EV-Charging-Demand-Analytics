import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../data/cleaned/EV_population_cleaned.csv")

# Count vehicle types
type_counts = df["Electric Vehicle Type"].value_counts()

print(type_counts)

# Plot pie chart
plt.figure()

type_counts.plot(kind="pie", autopct="%1.1f%%")

plt.title("EV Type Distribution")

plt.ylabel("")

# Save chart
plt.savefig("../outputs/charts/ev_type_distribution.png")

# Show chart
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load charging station dataset
stations = pd.read_csv("../data/raw/charging_stations.csv")

print("Columns in dataset:")
print(stations.columns)

# Select a column for analysis
column_name = stations.columns[0]

# Count values
counts = stations[column_name].value_counts().head(10)

print("\nTop values:")
print(counts)

# Plot chart
plt.figure()

counts.plot(kind="bar")

plt.title("Charging Station Distribution")
plt.xlabel(column_name)
plt.ylabel("Number of Stations")

plt.xticks(rotation=45)

plt.grid(True)

# Save chart
plt.savefig("../outputs/charts/charging_station_distribution.png")

plt.show()
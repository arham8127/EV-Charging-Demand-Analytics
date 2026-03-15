import pandas as pd

# Load dataset
stations = pd.read_csv("../data/raw/charging_stations.csv")

print("===== CHARGING STATION INSIGHTS =====\n")

# Total stations
print("Total Charging Stations:", len(stations))

# Most common charger type
top_charger = stations["Charger Type"].value_counts().idxmax()
print("Most Common Charger Type:", top_charger)

# Average charging capacity
avg_capacity = stations["Charging Capacity (kW)"].mean()
print("Average Charging Capacity:", round(avg_capacity, 2), "kW")

# Most common operator
top_operator = stations["Station Operator"].value_counts().idxmax()
print("Most Common Station Operator:", top_operator)

# Average usage per day
avg_usage = stations["Usage Stats (avg users/day)"].mean()
print("Average Daily Users:", round(avg_usage, 2))

print("\nCharging Station Analysis Completed!")
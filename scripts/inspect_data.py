import pandas as pd

# Load EV dataset
ev_data = pd.read_csv("../data/raw/EV_Population.csv")

# Load charging station dataset
station_data = pd.read_csv("../data/raw/charging_stations.csv")

print("===== EV DATASET INFO =====")

print("Shape:", ev_data.shape)

print("\nColumns:")
print(ev_data.columns)

print("\nFirst 5 rows:")
print(ev_data.head())

print("\nMissing values:")
print(ev_data.isnull().sum())


print("\n==============================\n")

print("===== CHARGING STATION DATA =====")

print("Shape:", station_data.shape)

print("\nColumns:")
print(station_data.columns)

print("\nFirst 5 rows:")
print(station_data.head())

print("\nMissing values:")
print(station_data.isnull().sum())
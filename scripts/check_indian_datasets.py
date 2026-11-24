
import pandas as pd
from pathlib import Path

# Project ka main folder identify karna
BASE_DIR = Path(__file__).resolve().parents[1]

# Naye synthetic datasets ka folder
DATA_DIR = BASE_DIR / "data" / "raw" / "synthetic_india"

# Dataset files
datasets = {
    "Charging Stations": "charging_stations_india.csv",
    "EV Population": "ev_population_india.csv",
    "Charging Demand": "charging_demand_india.csv",
    "City Demand Summary": "city_demand_summary_india.csv"
}

print("\n===================================")
print(" INDIAN EV DATASET VERIFICATION")
print("===================================\n")

for name, filename in datasets.items():

    file_path = DATA_DIR / filename

    if file_path.exists():

        df = pd.read_csv(file_path)

        print(f"Dataset: {name}")
        print("Rows:", len(df))
        print("Columns:", len(df.columns))
        print("Status: Successfully Loaded")

        if "City" in df.columns:
            print("Cities:", ", ".join(sorted(df["City"].dropna().unique())))

        print("-----------------------------------")

    else:
        print(f"ERROR: {filename} not found!")

print("\nDataset verification completed!")

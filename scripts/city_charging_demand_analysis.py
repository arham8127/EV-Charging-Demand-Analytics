
import os
import sys
import pandas as pd
from pathlib import Path

# Project root ko Python path mein add karna
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

import config

# =====================================
# LOAD INDIA CHARGING DEMAND DATA
# =====================================
df = pd.read_csv(config.INDIA_DEMAND_FILE)

# Date column ko datetime format mein convert karna
df["Date"] = pd.to_datetime(df["Date"])

# =====================================
# CITY-WISE DEMAND ANALYSIS
# =====================================
city_analysis = df.groupby(
    ["City", "State"]
).agg(
    Total_Charging_Sessions=("Charging_Sessions", "sum"),
    Total_Energy_Demand_kWh=("Total_Energy_Demand_kWh", "sum"),
    Avg_Daily_Sessions=("Charging_Sessions", "mean"),
    Avg_Daily_Energy_kWh=("Total_Energy_Demand_kWh", "mean")
).reset_index()

# Highest energy demand wale city ko top par rakhna
city_analysis = city_analysis.sort_values(
    by="Total_Energy_Demand_kWh",
    ascending=False
)

# =====================================
# DISPLAY RESULTS
# =====================================
print("\n======================================")
print(" INDIA EV CHARGING DEMAND ANALYSIS")
print("======================================")

print("\nCity-wise Charging Demand:\n")

print(city_analysis.to_string(index=False))

# =====================================
# SAVE ANALYSIS OUTPUT
# =====================================
OUTPUT_DIR = BASE_DIR / "outputs" / "india_analysis"

os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "city_charging_demand_analysis.csv"

city_analysis.to_csv(OUTPUT_FILE, index=False)

print("\nAnalysis successfully completed!")
print("Output saved at:", OUTPUT_FILE)
print("\nNote: All results are based on synthetic data.")

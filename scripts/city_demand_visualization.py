
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

# =====================================
# PROJECT PATHS
# =====================================
BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = (
    BASE_DIR
    / "outputs"
    / "india_analysis"
    / "city_charging_demand_analysis.csv"
)

OUTPUT_DIR = BASE_DIR / "outputs" / "india_analysis"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================
# LOAD ANALYSIS DATA
# =====================================
df = pd.read_csv(INPUT_FILE)

# =====================================
# GRAPH 1: CHARGING SESSIONS
# =====================================
plt.figure(figsize=(10, 6))

plt.bar(
    df["City"],
    df["Total_Charging_Sessions"]
)

plt.title("City-wise EV Charging Sessions")
plt.xlabel("City")
plt.ylabel("Total Charging Sessions")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "city_charging_sessions.png",
    dpi=300
)

plt.show()
plt.close()

# =====================================
# GRAPH 2: ENERGY DEMAND
# =====================================
plt.figure(figsize=(10, 6))

plt.bar(
    df["City"],
    df["Total_Energy_Demand_kWh"]
)

plt.title("City-wise EV Charging Energy Demand")
plt.xlabel("City")
plt.ylabel("Total Energy Demand (kWh)")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "city_energy_demand.png",
    dpi=300
)

plt.show()
plt.close()

print("\nBoth graphs generated successfully!")
print("Output folder:", OUTPUT_DIR)
print("Note: Visualizations use synthetic data.")

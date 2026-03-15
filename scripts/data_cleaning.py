import pandas as pd

# Load EV dataset
ev_data = pd.read_csv("../data/raw/EV_Population.csv")

print("Original Shape:", ev_data.shape)

# Remove duplicates
ev_data = ev_data.drop_duplicates()

# Check missing values
print("\nMissing Values:")
print(ev_data.isnull().sum())

# Select important columns
ev_data = ev_data[[
    "State",
    "Model Year",
    "Make",
    "Electric Vehicle Type",
    "Electric Range",
    "Base MSRP"
]]

# Save cleaned dataset
ev_data.to_csv("../data/cleaned/EV_population_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
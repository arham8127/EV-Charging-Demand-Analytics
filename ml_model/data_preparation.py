import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_path = os.path.join(BASE_DIR, "data", "cleaned", "EV_population_cleaned.csv")

df = pd.read_csv(input_path)

# Basic cleaning
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

print("Data cleaned:", df.shape)
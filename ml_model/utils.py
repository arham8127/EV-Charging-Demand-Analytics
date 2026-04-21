import os
import pandas as pd
import pickle

# -------------------------------
# PATH FUNCTIONS
# -------------------------------
def get_base_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_data_path(filename):
    return os.path.join(get_base_dir(), "data", "cleaned", filename)

def get_model_path(filename):
    return os.path.join(get_base_dir(), "ml_model", "models", filename)

# -------------------------------
# LOAD DATA
# -------------------------------
def load_data(filename="EV_population_cleaned.csv"):
    path = get_data_path(filename)
    return pd.read_csv(path)

# -------------------------------
# LOAD MODEL
# -------------------------------
def load_model(filename="model.pkl"):
    path = get_model_path(filename)
    with open(path, "rb") as f:
        return pickle.load(f)
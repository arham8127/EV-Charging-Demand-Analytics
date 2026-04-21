import pandas as pd
import pickle

# ✅ IMPORT CONFIG
from config import MODEL_RANGE, MODEL_PRICE

# -------------------------------
# LOAD MODELS
# -------------------------------
with open(MODEL_RANGE, "rb") as f:
    model_range = pickle.load(f)

with open(MODEL_PRICE, "rb") as f:
    model_price = pickle.load(f)

# -------------------------------
# SAMPLE INPUT (REAL FORMAT)
# -------------------------------
input_data = pd.DataFrame([{
    "State": "Washington",
    "Model Year": 2022,
    "Make": "Tesla",
    "Electric Vehicle Type": "Battery Electric Vehicle",
    "Base MSRP": 40000
}])

# -------------------------------
# PREDICTIONS
# -------------------------------
range_pred = model_range.predict(input_data)[0]
price_pred = model_price.predict(input_data)[0]

print("🔋 Predicted Range:", range_pred)
print("💰 Predicted Price:", price_pred)
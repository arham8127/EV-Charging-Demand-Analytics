import pandas as pd
import pickle

from sklearn.metrics import mean_absolute_error, r2_score

# ✅ IMPORT CONFIG
from config import DATA_FILE, MODEL_RANGE, MODEL_PRICE

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv(DATA_FILE)

# -------------------------------
# FEATURES
# -------------------------------
X = df.drop(["Electric Range", "Base MSRP"], axis=1)

# Targets
y_range = df["Electric Range"]
y_price = df["Base MSRP"]

# -------------------------------
# LOAD MODELS
# -------------------------------
with open(MODEL_RANGE, "rb") as f:
    model_range = pickle.load(f)

with open(MODEL_PRICE, "rb") as f:
    model_price = pickle.load(f)

# -------------------------------
# EVALUATION FUNCTION
# -------------------------------
def evaluate(model, X, y, name):
    y_pred = model.predict(X)

    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    print(f"\n📊 {name} Model Performance")
    print(f"MAE: {mae:.4f}")
    print(f"R2 Score: {r2:.4f}")


# -------------------------------
# EVALUATE BOTH MODELS
# -------------------------------
evaluate(model_range, X, y_range, "Range 🔋")
evaluate(model_price, X, y_price, "Price 💰")
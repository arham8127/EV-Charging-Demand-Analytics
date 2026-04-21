import pandas as pd
import pickle
import os
import sys

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# -------------------------------
# FIX PATH (for config import)
# -------------------------------
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# -------------------------------
# IMPORT CONFIG
# -------------------------------
from config import (
    DATA_FILE,
    MODEL_RANGE,
    MODEL_PRICE,
    TARGET,
    PRICE_TARGET,
    CATEGORICAL_FEATURES,
    NUMERICAL_FEATURES,
    TEST_SIZE,
    RANDOM_STATE,
    N_ESTIMATORS
)

# -------------------------------
# CREATE MODEL DIR
# -------------------------------
os.makedirs(os.path.dirname(MODEL_RANGE), exist_ok=True)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv(DATA_FILE)
print("✅ Data Loaded:", df.shape)

# -------------------------------
# FEATURES
# -------------------------------
X = df[CATEGORICAL_FEATURES + NUMERICAL_FEATURES]

# Targets
y_range = df[TARGET]
y_price = df[PRICE_TARGET]

# -------------------------------
# PREPROCESSING
# -------------------------------
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
    ("num", "passthrough", NUMERICAL_FEATURES)
])

# -------------------------------
# TRAIN FUNCTION
# -------------------------------
def train_and_save(X, y, model_path, name):

    print(f"\n🚀 Training {name} Model...")

    model = RandomForestRegressor(
        n_estimators=N_ESTIMATORS,
        random_state=RANDOM_STATE
    )

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", model)
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    pipeline.fit(X_train, y_train)

    with open(model_path, "wb") as f:
        pickle.dump(pipeline, f)

    print(f"✅ {name} Model Saved at: {model_path}")


# -------------------------------
# TRAIN BOTH MODELS
# -------------------------------
train_and_save(X, y_range, MODEL_RANGE, "Range 🔋")
train_and_save(X, y_price, MODEL_PRICE, "Price 💰")

print("\n🔥 Both models trained successfully!")
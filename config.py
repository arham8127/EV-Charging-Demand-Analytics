import os

# -------------------------------
# BASE PATH
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------------
# DATA PATH
# -------------------------------
DATA_FILE = os.path.join(BASE_DIR, "data", "cleaned", "EV_population_cleaned.csv")

# -------------------------------
# MODEL PATHS (🔥 UPGRADED)
# -------------------------------
MODEL_FILE = os.path.join(BASE_DIR, "ml_model", "models", "model.pkl")  # old (optional)

MODEL_RANGE = os.path.join(BASE_DIR, "ml_model", "models", "model_range.pkl")
MODEL_PRICE = os.path.join(BASE_DIR, "ml_model", "models", "model_price.pkl")

# -------------------------------
# ASSETS
# -------------------------------
MAIN_BG = os.path.join(BASE_DIR, "assets", "ev_banner.jpg")
NAVBAR_BG = os.path.join(BASE_DIR, "assets", "navbar_bg_img.jpg")

# -------------------------------
# FEATURES
# -------------------------------
TARGET = "Electric Range"   # default (range model)

PRICE_TARGET = "Base MSRP"  # 🔥 new

CATEGORICAL_FEATURES = [
    "State",
    "Make",
    "Electric Vehicle Type"
]

NUMERICAL_FEATURES = [
    "Model Year",
    "Base MSRP"
]

# -------------------------------
# MODEL SETTINGS
# -------------------------------
TEST_SIZE = 0.2
RANDOM_STATE = 42
N_ESTIMATORS = 100
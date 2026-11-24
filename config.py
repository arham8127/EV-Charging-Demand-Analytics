
import os

# =====================================
# BASE PATH
# =====================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =====================================
# OLD DATASET PATH (EXISTING PROJECT)
# =====================================
DATA_FILE = os.path.join(
    BASE_DIR,
    "data",
    "cleaned",
    "EV_population_cleaned.csv"
)


# =====================================
# INDIA SYNTHETIC DATASET PATHS
# =====================================
INDIA_DATA_DIR = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "synthetic_india"
)

# 1. Charging Stations Dataset
INDIA_STATIONS_FILE = os.path.join(
    INDIA_DATA_DIR,
    "charging_stations_india.csv"
)

# 2. EV Population Dataset
INDIA_POPULATION_FILE = os.path.join(
    INDIA_DATA_DIR,
    "ev_population_india.csv"
)

# 3. Daily Charging Demand Dataset
INDIA_DEMAND_FILE = os.path.join(
    INDIA_DATA_DIR,
    "charging_demand_india.csv"
)

# 4. City-wise Demand Summary Dataset
INDIA_CITY_SUMMARY_FILE = os.path.join(
    INDIA_DATA_DIR,
    "city_demand_summary_india.csv"
)


# =====================================
# MODEL PATHS (EXISTING ML MODELS)
# =====================================
MODEL_FILE = os.path.join(
    BASE_DIR, "ml_model", "models", "model.pkl"
)

MODEL_RANGE = os.path.join(
    BASE_DIR, "ml_model", "models", "model_range.pkl"
)

MODEL_PRICE = os.path.join(
    BASE_DIR, "ml_model", "models", "model_price.pkl"
)


# =====================================
# ASSETS
# =====================================
MAIN_BG = os.path.join(
    BASE_DIR, "assets", "ev_banner.jpg"
)

NAVBAR_BG = os.path.join(
    BASE_DIR, "assets", "navbar_bg_img.jpg"
)


# =====================================
# FEATURES (EXISTING ML PROJECT)
# =====================================
TARGET = "Electric Range"

PRICE_TARGET = "Base MSRP"

CATEGORICAL_FEATURES = [
    "State",
    "Make",
    "Electric Vehicle Type"
]

NUMERICAL_FEATURES = [
    "Model Year",
    "Base MSRP"
]


# =====================================
# MODEL SETTINGS
# =====================================
TEST_SIZE = 0.2

RANDOM_STATE = 42

N_ESTIMATORS = 100


# =====================================
# INDIA PROJECT CITIES
# =====================================
INDIAN_CITIES = [
    "Lucknow",
    "Delhi",
    "Mumbai",
    "Pune",
    "Bengaluru"
]


# =====================================
# DATASET TYPE
# =====================================
DATA_TYPE = "SYNTHETIC"

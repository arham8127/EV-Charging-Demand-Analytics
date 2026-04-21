import streamlit as st
import pandas as pd
import pickle
import os
import base64

# -------------------------------
# IMPORT CONFIG
# -------------------------------
from config import DATA_FILE, MODEL_RANGE, MODEL_PRICE

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="EV Prediction System",
    page_icon="⚡",
    layout="wide"
)

# -------------------------------
# BACKGROUND FUNCTION (STABLE)
# -------------------------------
def set_dynamic_bg(images):

    def get_base64(img_path):
        if not os.path.exists(img_path):
            return ""
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    if "bg_index" not in st.session_state:
        st.session_state.bg_index = 0

    img_path = images[st.session_state.bg_index % len(images)]
    encoded_bg = get_base64(img_path)

    # 🔥 NAVBAR IMAGE LOAD
    navbar_path = os.path.join(BASE_DIR, "assets", "navbar_bg_img.jpg")
    encoded_nav = get_base64(navbar_path)

    st.markdown(f"""
    <style>

    /* BACKGROUND */
    .stApp {{
        background: url("data:image/jpg;base64,{encoded_bg}") no-repeat center center fixed;
        background-size: cover;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.4);
        z-index: 0;
    }}

    .block-container {{
        position: relative;
        z-index: 1;
    }}

    /* 🔥 NAVBAR BACKGROUND */
    header[data-testid="stHeader"] {{
        background: url("data:image/jpg;base64,{encoded_nav}") no-repeat center !important;
        background-size: cover !important;
    }}

    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}

    </style>
    """, unsafe_allow_html=True)

    st.session_state.bg_index += 1


# -------------------------------
# APPLY BACKGROUND
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

images = [
    os.path.join(BASE_DIR, "assets", "ev_banner.jpg"),
    os.path.join(BASE_DIR, "assets", "ev_banner2.jpg"),
    os.path.join(BASE_DIR, "assets", "ev_banner3.jpg"),
    os.path.join(BASE_DIR, "assets", "ev_banner4.jpg"),
]

# ✅ CORRECT FUNCTION CALL
set_dynamic_bg(images)

# -------------------------------
# LOAD MODELS (SAFE)
# -------------------------------
if not os.path.exists(MODEL_RANGE):
    st.error("❌ Range model not found! Run training first.")
    st.stop()

if not os.path.exists(MODEL_PRICE):
    st.error("❌ Price model not found! Run training first.")
    st.stop()

with open(MODEL_RANGE, "rb") as f:
    model_range = pickle.load(f)

with open(MODEL_PRICE, "rb") as f:
    model_price = pickle.load(f)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv(DATA_FILE)

# -------------------------------
# CLEAN STATES
# -------------------------------
df["State"] = df["State"].astype(str).str.strip()

state_mapping = {
    "WA": "Washington",
    "CA": "California",
    "TX": "Texas",
    "NY": "New York"
}

df["State"] = df["State"].map(state_mapping).fillna(df["State"])

dataset_states = df["State"].dropna().unique().tolist()

extra_states = [
    "Washington", "California", "Texas", "New York",
    "Florida", "Illinois", "Georgia", "Ohio"
]

states = sorted(list(set(dataset_states + extra_states)))

# -------------------------------
# DROPDOWNS
# -------------------------------
makes = sorted(df["Make"].dropna().unique())
ev_types = sorted(df["Electric Vehicle Type"].dropna().unique())

# -------------------------------
# TITLE
# -------------------------------
st.title("⚡ EV Prediction System")
st.markdown("### Predict EV Range & Price using Machine Learning")

# -------------------------------
# UI
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Details")
    state = st.selectbox("State", states)
    make = st.selectbox("Make", makes)
    ev_type = st.selectbox("EV Type", ev_types)

with col2:
    st.subheader("⚙️ Specifications")
    year = st.slider(
        "Model Year",
        int(df["Model Year"].min()),
        int(df["Model Year"].max()),
        2022
    )
    price = st.number_input(
        "Base MSRP",
        int(df["Base MSRP"].min()),
        int(df["Base MSRP"].max()),
        40000
    )

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("🚀 Predict"):

    input_data = pd.DataFrame([{
        "State": state,
        "Model Year": year,
        "Make": make,
        "Electric Vehicle Type": ev_type,
        "Base MSRP": price
    }])

    range_pred = model_range.predict(input_data)[0]
    price_pred = model_price.predict(input_data)[0]

    st.success(f"🔋 Predicted Range: {range_pred:.2f}")
    st.success(f"💰 Predicted Price: {price_pred:.2f}")
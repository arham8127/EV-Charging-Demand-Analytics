
import streamlit as st
import pandas as pd
import pickle
import os
import base64

# =====================================
# IMPORT CONFIG
# =====================================
from config import (
    DATA_FILE,
    MODEL_RANGE,
    MODEL_PRICE,
    INDIA_STATIONS_FILE,
    INDIA_POPULATION_FILE,
    INDIA_DEMAND_FILE,
    INDIA_CITY_SUMMARY_FILE
)

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="EV Analytics & Prediction System",
    page_icon="⚡",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =====================================
# BACKGROUND FUNCTION
# =====================================
def set_dynamic_bg(images):

    def get_base64(img_path):
        if not os.path.exists(img_path):
            return ""

        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    if "bg_index" not in st.session_state:
        st.session_state.bg_index = 0

    img_path = images[
        st.session_state.bg_index % len(images)
    ]

    encoded_bg = get_base64(img_path)

    navbar_path = os.path.join(
        BASE_DIR, "assets", "navbar_bg_img.jpg"
    )

    encoded_nav = get_base64(navbar_path)

    st.markdown(f"""
    <style>

    .stApp {{
        background: url("data:image/jpg;base64,{encoded_bg}")
        no-repeat center center fixed;
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

    header[data-testid="stHeader"] {{
        background: url("data:image/jpg;base64,{encoded_nav}")
        no-repeat center !important;
        background-size: cover !important;
    }}

    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}

    </style>
    """, unsafe_allow_html=True)

    st.session_state.bg_index += 1


# =====================================
# APPLY BACKGROUND
# =====================================
images = [
    os.path.join(BASE_DIR, "assets", "ev_banner.jpg"),
    os.path.join(BASE_DIR, "assets", "ev_banner2.jpg"),
    os.path.join(BASE_DIR, "assets", "ev_banner3.jpg"),
    os.path.join(BASE_DIR, "assets", "ev_banner4.jpg")
]

set_dynamic_bg(images)


# =====================================
# LOAD OLD ML MODELS
# =====================================
model_range = None
model_price = None

if os.path.exists(MODEL_RANGE):
    with open(MODEL_RANGE, "rb") as f:
        model_range = pickle.load(f)

if os.path.exists(MODEL_PRICE):
    with open(MODEL_PRICE, "rb") as f:
        model_price = pickle.load(f)


# =====================================
# LOAD OLD DATASET
# =====================================
df = None

if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)


# =====================================
# LOAD INDIA DATASETS
# =====================================
stations_df = pd.read_csv(INDIA_STATIONS_FILE)
population_df = pd.read_csv(INDIA_POPULATION_FILE)
demand_df = pd.read_csv(INDIA_DEMAND_FILE)
summary_df = pd.read_csv(INDIA_CITY_SUMMARY_FILE)

demand_df["Date"] = pd.to_datetime(demand_df["Date"])
population_df["Month"] = pd.to_datetime(
    population_df["Month"]
)


# =====================================
# MAIN TITLE
# =====================================
st.title("⚡ EV Analytics & Prediction System")

st.markdown(
    "### Electric Vehicle Prediction and India Charging Demand Analytics"
)

st.caption(
    "India analytics section uses simulated synthetic datasets."
)


# =====================================
# DASHBOARD NAVIGATION
# =====================================
page = st.sidebar.radio(
    "Select Dashboard",
    [
        "India EV Analytics",
        "EV Range & Price Prediction"
    ]
)


# =====================================
# PAGE 1: INDIA EV ANALYTICS
# =====================================
if page == "India EV Analytics":

    st.header("🇮🇳 India EV Charging Demand Dashboard")

    st.info(
        "Note: All India city-wise results shown here "
        "are based on synthetic data, not official measurements."
    )

    # ---------------------------------
    # CITY-WISE SUMMARY
    # ---------------------------------
    total_sessions = int(
        summary_df["Total_Sessions_6M"].sum()
    )

    total_energy = summary_df[
        "Total_Energy_Demand_6M_kWh"
    ].sum()

    total_stations = len(stations_df)

    total_cities = summary_df["City"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Charging Sessions",
        f"{total_sessions:,}"
    )

    col2.metric(
        "Total Energy Demand",
        f"{total_energy:,.0f} kWh"
    )

    col3.metric(
        "Charging Stations",
        f"{total_stations:,}"
    )

    col4.metric(
        "Cities Covered",
        total_cities
    )

    st.divider()

    # ---------------------------------
    # CITY-WISE COMPARISON
    # ---------------------------------
    st.subheader("📊 City-wise Charging Demand")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Charging Sessions")

        sessions_chart = summary_df.set_index("City")[
            ["Total_Sessions_6M"]
        ]

        st.bar_chart(sessions_chart)

    with col2:
        st.markdown("#### Energy Demand (kWh)")

        energy_chart = summary_df.set_index("City")[
            ["Total_Energy_Demand_6M_kWh"]
        ]

        st.bar_chart(energy_chart)

    st.divider()

    # ---------------------------------
    # CITY SELECTION
    # ---------------------------------
    st.subheader("🏙️ Individual City Analysis")

    selected_city = st.selectbox(
        "Select a City",
        sorted(demand_df["City"].unique())
    )

    city_demand = demand_df[
        demand_df["City"] == selected_city
    ].sort_values("Date")

    city_stations = stations_df[
        stations_df["City"] == selected_city
    ]

    city_population = population_df[
        population_df["City"] == selected_city
    ].sort_values("Month")

    # ---------------------------------
    # SELECTED CITY METRICS
    # ---------------------------------
    city_sessions = int(
        city_demand["Charging_Sessions"].sum()
    )

    city_energy = city_demand[
        "Total_Energy_Demand_kWh"
    ].sum()

    city_station_count = len(city_stations)

    city_latest_population = int(
        city_population.iloc[-1][
            "Estimated_EV_Population"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Charging Sessions",
        f"{city_sessions:,}"
    )

    col2.metric(
        "Energy Demand",
        f"{city_energy:,.0f} kWh"
    )

    col3.metric(
        "Charging Stations",
        city_station_count
    )

    col4.metric(
        "Estimated EV Population",
        f"{city_latest_population:,}"
    )

    # ---------------------------------
    # DAILY DEMAND TREND
    # ---------------------------------
    st.subheader(
        f"📈 Daily Charging Demand - {selected_city}"
    )

    daily_chart = city_demand.set_index("Date")[
        ["Charging_Sessions"]
    ]

    st.line_chart(daily_chart)


    # ---------------------------------
    # PEAK CHARGING DEMAND ANALYSIS
    # ---------------------------------
    st.subheader(
        f"⏰ Peak Charging Demand - {selected_city}"
    )

    peak_analysis = city_demand.groupby(
        "Peak_Demand_Period"
    ).agg(
        Total_Sessions=("Charging_Sessions", "sum"),
        Total_Energy=("Total_Energy_Demand_kWh", "sum")
    ).reset_index()

    peak_analysis = peak_analysis.sort_values(
        by="Total_Sessions",
        ascending=False
    )

    # Highest demand period
    peak_period = peak_analysis.iloc[0]

    st.success(
        f"Highest charging demand period: "
        f"{peak_period['Peak_Demand_Period']}"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Sessions by Time Period")

        st.bar_chart(
            peak_analysis.set_index("Peak_Demand_Period")[
                ["Total_Sessions"]
            ]
        )

    with col2:
        st.markdown("#### Energy Demand by Time Period")

        st.bar_chart(
            peak_analysis.set_index("Peak_Demand_Period")[
                ["Total_Energy"]
            ]
        )

    st.dataframe(
        peak_analysis,
        use_container_width=True
    )

    # ---------------------------------
    # ENERGY TREND
    # ---------------------------------
    st.subheader(
        f"⚡ Daily Energy Consumption - {selected_city}"
    )

    energy_trend = city_demand.set_index("Date")[
        ["Total_Energy_Demand_kWh"]
    ]

    st.line_chart(energy_trend)

    st.divider()

    # ---------------------------------
    # EV POPULATION GROWTH
    # ---------------------------------
    st.subheader(
        f"🚗 EV Population Growth - {selected_city}"
    )

    population_chart = city_population.set_index("Month")[
        ["Estimated_EV_Population"]
    ]

    st.line_chart(population_chart)

    # ---------------------------------
    # CHARGING STATION DETAILS
    # ---------------------------------
    st.subheader(
        f"🔌 Charging Stations - {selected_city}"
    )

    st.dataframe(
        city_stations,
        use_container_width=True
    )

    # ---------------------------------
    # CITY SUMMARY TABLE
    # ---------------------------------
    st.subheader("📋 All Cities Summary")

    st.dataframe(
        summary_df,
        use_container_width=True
    )


# =====================================
# PAGE 2: OLD EV PREDICTION SYSTEM
# =====================================
elif page == "EV Range & Price Prediction":

    st.header("🔋 EV Range & Price Prediction")

    if df is None:
        st.error("Old EV dataset not found!")
        st.stop()

    if model_range is None or model_price is None:
        st.error(
            "Prediction models not found. "
            "Please train the models first."
        )
        st.stop()

    # ---------------------------------
    # CLEAN STATES
    # ---------------------------------
    df["State"] = df["State"].astype(str).str.strip()

    state_mapping = {
        "WA": "Washington",
        "CA": "California",
        "TX": "Texas",
        "NY": "New York"
    }

    df["State"] = (
        df["State"].map(state_mapping).fillna(df["State"])
    )

    dataset_states = df["State"].dropna().unique().tolist()

    extra_states = [
        "Washington", "California", "Texas", "New York",
        "Florida", "Illinois", "Georgia", "Ohio"
    ]

    states = sorted(
        list(set(dataset_states + extra_states))
    )

    makes = sorted(df["Make"].dropna().unique())
    ev_types = sorted(
        df["Electric Vehicle Type"].dropna().unique()
    )

    # ---------------------------------
    # INPUT DETAILS
    # ---------------------------------
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

    # ---------------------------------
    # PREDICTION
    # ---------------------------------
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

        st.success(
            f"🔋 Predicted Range: {range_pred:.2f}"
        )

        st.success(
            f"💰 Predicted Price: {price_pred:.2f}"
        )


# =====================================
# FOOTER
# =====================================
st.divider()

st.caption(
    "EV Analytics & Prediction System | "
    "India city-wise analytics are based on synthetic data."
)

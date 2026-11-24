# ⚡ EV Charging Demand Analytics

## Project Overview

EV Charging Demand Analytics is a data analytics and machine learning project designed to study Electric Vehicle (EV) adoption trends, predict EV specifications, and analyze charging demand across selected Indian cities.

The project combines data analysis, visualization, and machine learning to provide insights into EV growth and charging infrastructure requirements.

The India-focused analytics module covers five major cities:

- Lucknow, Uttar Pradesh
- Delhi
- Mumbai, Maharashtra
- Pune, Maharashtra
- Bengaluru, Karnataka

**Important:** The India-focused datasets used in this project are synthetically generated for demonstration and analytical purposes. They do not represent actual measured charging sessions, official EV registrations, or verified charging station records.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Scikit-learn
- Machine Learning
- CSV Data Processing

---

## Key Features

### 1. EV Range Prediction
Predicts the estimated driving range of an electric vehicle using machine learning.

### 2. EV Price Prediction
Estimates EV prices based on vehicle specifications and available input features.

### 3. City-wise Charging Demand Analysis
Analyzes estimated EV charging demand across five Indian cities.

### 4. Charging Sessions Analysis
Compares the number of simulated charging sessions across different cities.

### 5. Energy Demand Analysis
Analyzes estimated electricity consumption measured in kilowatt-hours (kWh).

### 6. Peak Charging Demand Analysis
Identifies simulated time periods with the highest charging activity.

### 7. EV Population Growth Analysis
Visualizes estimated EV population trends across selected cities.

### 8. Charging Station Overview
Displays simulated charging station information, charger types, and capacities.

---

## Dataset Information

The India-focused module uses four synthetic datasets:

| Dataset | Records | Description |
|---|---:|---|
| charging_stations_india.csv | 500 | Simulated charging station details |
| charging_demand_india.csv | 920 | Daily charging demand records |
| ev_population_india.csv | 30 | Monthly estimated EV population |
| city_demand_summary_india.csv | 5 | City-wise demand summary |

### Dataset Period
May 2026 – October 2026

### Cities Covered
1. Lucknow
2. Delhi
3. Mumbai
4. Pune
5. Bengaluru

### Important Metrics

- **Charging Sessions:** Number of simulated EV charging events.
- **Total Energy Demand:** Estimated electricity consumption measured in kWh.
- **EV Population:** Simulated estimated EV population.
- **Charging Stations:** Simulated charging station records.

---

## Project Structure

```text
EV-Charging-Demand-Analytics/
│
├── app.py
├── config.py
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── synthetic_india/
│   │       ├── charging_stations_india.csv
│   │       ├── charging_demand_india.csv
│   │       ├── ev_population_india.csv
│   │       └── city_demand_summary_india.csv
│   │
│   └── cleaned/
│
├── scripts/
│   ├── check_indian_datasets.py
│   ├── city_charging_demand_analysis.py
│   ├── city_demand_visualization.py
│   ├── ev growth analysis.py
│   ├── ev range analysis.py
│   └── ev type analysis.py
│
├── ml_model/
│   └── models/
│
├── outputs/
│   └── india_analysis/
│       ├── city_charging_demand_analysis.csv
│       ├── city_charging_sessions.png
│       └── city_energy_demand.png
│
└── assets/
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/arham8127/EV-Charging-Demand-Analytics.git
```

### 2. Navigate to Project Folder

```bash
cd EV-Charging-Demand-Analytics
```

### 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib streamlit scikit-learn
```

### 4. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

---

## Dashboard Modules

The Streamlit dashboard provides two main modules:

### 1. India EV Analytics

- City-wise charging demand analysis
- Charging sessions comparison
- Energy consumption analysis
- Individual city selection
- Peak charging demand analysis
- EV population growth visualization
- Charging station details

### 2. EV Range & Price Prediction

- Vehicle specification inputs
- EV range prediction
- EV price prediction

---

## Output and Results

The project generates:

- City-wise charging demand analysis CSV
- Charging sessions comparison graph
- Energy demand comparison graph
- Interactive Streamlit dashboard
- City-wise demand insights

---

## Future Improvements

1. Integration of real-world EV registration data.
2. Integration of verified charging station locations.
3. Real-time charging station availability.
4. Advanced EV charging demand forecasting.
5. Interactive geographical maps.
6. Hourly charging demand prediction.
7. Integration of weather and traffic data.
8. Improved machine learning models.

---

## Limitations

- The India-focused datasets are synthetic and generated for project demonstration.
- The results should not be interpreted as official statistics or actual charging infrastructure measurements.
- Charging station coordinates are simulated and should not be treated as verified locations.
- Future versions can incorporate verified public datasets and real-world charging information to improve analytical accuracy.

---

## Conclusion

This project demonstrates how data analytics, visualization, and machine learning can be used to understand EV adoption patterns and estimate charging infrastructure requirements.

By combining EV prediction features with city-wise charging demand analysis, the project provides a foundation for further research and development in electric vehicle analytics and smart charging infrastructure planning.

---

## Author

**Arham Ali**

GitHub: https://github.com/arham8127
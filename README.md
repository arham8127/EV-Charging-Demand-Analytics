# India EV Charging Demand Analytics

## Project Overview

The EV Charging Demand Analytics project is designed to analyze Electric Vehicle (EV) charging demand across five major Indian cities:

- Lucknow
- Delhi
- Mumbai
- Pune
- Bengaluru

The project combines data analysis, visualization, and machine learning-based EV prediction features to provide insights into EV adoption and charging infrastructure requirements.

**Important:** The India city-wise datasets used in this project are synthetically generated for demonstration and analytical purposes. They do not represent actual measured charging sessions, official EV registrations, or verified charging station records.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Scikit-learn
- Machine Learning
- CSV Data Processing

## Key Features

### 1. EV Range Prediction
Predicts the estimated driving range of an electric vehicle using machine learning.

### 2. EV Price Prediction
Estimates EV prices based on vehicle specifications and available input features.

### 3. City-wise Charging Demand Analysis
Analyzes estimated EV charging demand across five Indian cities.

### 4. Charging Sessions Analysis
Compares the number of charging sessions across different cities.

### 5. Energy Demand Analysis
Measures estimated electricity consumption in kilowatt-hours (kWh).

### 6. Peak Charging Demand Analysis
Identifies the simulated time periods with the highest charging activity.

### 7. EV Population Growth Analysis
Visualizes estimated EV population trends across the selected cities.

### 8. Charging Station Overview
Displays simulated charging station information, charger types, and capacities.

## Dataset Information

The project uses four synthetic India-focused datasets:

| Dataset | Records | Description |
|---|---:|---|
| charging_stations_india.csv | 500 | Simulated charging station details |
| charging_demand_india.csv | 920 | Daily charging demand records |
| ev_population_india.csv | 30 | Monthly estimated EV population |
| city_demand_summary_india.csv | 5 | City-wise demand summary |

### Dataset Period

May 2026 – October 2026

### Cities Covered

1. Lucknow, Uttar Pradesh
2. Delhi
3. Mumbai, Maharashtra
4. Pune, Maharashtra
5. Bengaluru, Karnataka

### Important Metrics

- Charging Sessions: Number of simulated EV charging events.
- Total Energy Demand: Estimated electricity consumption measured in kWh.
- EV Population: Simulated estimated EV population.
- Charging Stations: Simulated charging station records.

## Project Structure

```text
EV-Charging-Demand-Analytics/
│
├── app.py
├── config.py
├── README.md
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
│   ├── ev growth analysis.py
│   ├── ev range analysis.py
│   ├── ev type analysis.py
│   ├── check_indian_datasets.py
│   ├── city_charging_demand_analysis.py
│   └── city_demand_visualization.py
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

## Dashboard Modules

The Streamlit dashboard provides two main modules:

**1. India EV Analytics**
- City-wise charging demand
- Charging sessions comparison
- Energy consumption analysis
- Individual city selection
- Peak charging demand
- EV population growth
- Charging station details

**2. EV Range & Price Prediction**
- Vehicle specification inputs
- EV range prediction
- EV price prediction

## Output and Results

The project generates:

- City-wise charging demand analysis CSV
- Charging sessions comparison graph
- Energy demand comparison graph
- Interactive Streamlit dashboard

## Future Improvements

1. Integration of real-world EV registration data.
2. Integration of verified charging station locations.
3. Real-time charging station availability.
4. Advanced EV charging demand forecasting.
5. Interactive geographical maps.
6. Hourly charging demand prediction.
7. Integration of weather and traffic data.
8. Improved machine learning models.

## Limitations

The India-focused datasets are synthetic and generated for project demonstration. The results should not be interpreted as official statistics or actual charging infrastructure measurements.

Future versions can incorporate verified public datasets and real-world charging information to improve analytical accuracy.

## Conclusion

This project demonstrates how data analytics, visualization, and machine learning can be used to understand EV adoption patterns and estimate charging infrastructure requirements across Indian cities.

It provides a foundation for further research and development in electric vehicle charging demand analysis.

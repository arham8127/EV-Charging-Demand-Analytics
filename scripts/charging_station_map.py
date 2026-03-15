import pandas as pd
import folium

# Load dataset
stations = pd.read_csv("../data/raw/charging_stations.csv")

# Create base map
map_ev = folium.Map(location=[20, 0], zoom_start=2)

# Add markers (limit to first 200 for performance)
for i, row in stations.head(200).iterrows():

    if "Latitude" in stations.columns and "Longitude" in stations.columns:

        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup="Charging Station"
        ).add_to(map_ev)

# Save map
map_ev.save("../outputs/charging_station_map.html")

print("Map created successfully!")
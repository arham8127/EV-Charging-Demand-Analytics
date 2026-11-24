
import os
import csv
import json
import requests

from pathlib import Path
from dotenv import load_dotenv


# ==========================================
# 1. PROJECT PATH AND API CONFIGURATION
# ==========================================

# Project root folder ka path
BASE_DIR = Path(__file__).resolve().parents[2]

# .env file se API key load karna
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("OPENCHARGEMAP_API_KEY")

API_URL = "https://api.openchargemap.io/v3/poi/"


# ==========================================
# 2. CITIES AND THEIR COORDINATES
# ==========================================

CITIES = {
    "Lucknow": (26.8467, 80.9462),
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Pune": (18.5204, 73.8567),
    "Bengaluru": (12.9716, 77.5946)
}


# ==========================================
# 3. OUTPUT FOLDER
# ==========================================

OUTPUT_DIR = BASE_DIR / "data" / "raw" / "open_charge_map"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================
# 4. FETCH STATIONS FROM API
# ==========================================

def fetch_city_stations(city, latitude, longitude):

    print("\nFetching data for:", city)

    params = {
        "key": API_KEY,
        "output": "json",
        "countrycode": "IN",
        "latitude": latitude,
        "longitude": longitude,
        "distance": 30,
        "distanceunit": "KM",
        "maxresults": 500
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=60
    )

    response.raise_for_status()

    stations = response.json()

    print(city, "stations found:", len(stations))

    return stations


# ==========================================
# 5. CONVERT API DATA INTO CSV ROWS
# ==========================================

def clean_station_data(city, stations):

    cleaned_data = []

    for station in stations:

        address = station.get("AddressInfo") or {}
        operator = station.get("OperatorInfo") or {}
        status = station.get("StatusType") or {}
        country = address.get("Country") or {}

        connections = station.get("Connections") or []

        charger_types = []

        for connection in connections:

            connection_type = connection.get("ConnectionType") or {}

            charger_types.append(
                connection_type.get("Title", "Unknown")
            )

        row = {
            "City": city,
            "Station_ID": station.get("ID"),
            "Station_Name": address.get("Title"),
            "Address": address.get("AddressLine1"),
            "Town": address.get("Town"),
            "State": address.get("StateOrProvince"),
            "Country": country.get("Title"),
            "Latitude": address.get("Latitude"),
            "Longitude": address.get("Longitude"),
            "Operator": operator.get("Title"),
            "Status": status.get("Title"),
            "Charger_Types": ", ".join(charger_types),
            "Number_of_Connections": len(connections),
            "Usage_Cost": station.get("UsageCost")
        }

        cleaned_data.append(row)

    return cleaned_data


# ==========================================
# 6. MAIN FUNCTION
# ==========================================

def main():

    if not API_KEY:
        print("ERROR: API key not found in .env file.")
        return

    all_stations = []

    for city, coordinates in CITIES.items():

        latitude, longitude = coordinates

        try:
            stations = fetch_city_stations(
                city,
                latitude,
                longitude
            )

            # Original API response JSON save karna
            json_path = OUTPUT_DIR / f"{city.lower()}_stations.json"

            with open(json_path, "w", encoding="utf-8") as file:
                json.dump(stations, file, indent=4)

            # CSV format mein convert karna
            cleaned_data = clean_station_data(city, stations)

            all_stations.extend(cleaned_data)

        except requests.RequestException as error:
            print("API error for", city, ":", error)

        except (ValueError, TypeError) as error:
            print("Data error for", city, ":", error)

    # Combined CSV file save karna
    if all_stations:

        csv_path = OUTPUT_DIR / "india_charging_stations.csv"

        with open(csv_path, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=all_stations[0].keys()
            )

            writer.writeheader()
            writer.writerows(all_stations)

        print("\nData collection completed!")
        print("Total stations collected:", len(all_stations))
        print("CSV saved at:", csv_path)

    else:
        print("\nNo station data collected.")


# ==========================================
# 7. RUN PROGRAM
# ==========================================

if __name__ == "__main__":
    main()

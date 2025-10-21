import requests
import pandas as pd

# I get weather data from Open-Meteo API
def fetch_open_meteo(lat: float, lon: float, start: str, end: str):
    """Fetch daily weather data from the Open-Meteo API."""

# Build the API URL
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&daily=temperature_2m_max,temperature_2m_min,windspeed_10m_max"
        f"&start_date={start}&end_date={end}&timezone=auto"
    )

# Send the request and check for errors
    response = requests.get(url, timeout=20)
    response.raise_for_status()

# Read the data from the JSON response
    data = response.json()["daily"]

# Make a dataframe with data, temperatures, and wind
    df = pd.DataFrame({
        "date": pd.to_datetime(data["time"]),
        "tmax": data["temperature_2m_max"],
        "tmin": data["temperature_2m_min"],
        "windmax": data["windspeed_10m_max"]
    })

# Return the data
    return df

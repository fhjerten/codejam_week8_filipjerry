import pandas as pd

# Load weather data and find average temperatures
def load_weather_csv(path: str):
    """Read a weather CSV file and calculate average temperatures."""

# Read CSV and make data a date type
    df = pd.read_csv(path, parse_dates=["date"])

# Drop rows missing tmax or tmin 
    df = df.dropna(subset=["tmax", "tmin"])

# Make new column for average temperature
    df["tavg"] = (df["tmax"] + df["tmin"]) / 2

# Return needed columns only
    return df[["date", "tmin", "tmax", "tavg"]]

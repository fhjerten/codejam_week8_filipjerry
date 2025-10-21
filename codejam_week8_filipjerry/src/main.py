from pathlib import Path
from datetime import date, timedelta
import pandas as pd
from generate import simulate_golf_rounds
from fetch_api import fetch_open_meteo
from download_csv import load_weather_csv
from visualize import line_scores, scatter_wind_vs_score

# Set up folders for raw and processed data
DATA_RAW = Path("data/raw")
DATA_PRO = Path("data/processed")
DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_PRO.mkdir(parents=True, exist_ok=True)

def run_pipeline():
# 1. Generate fake golf data
    rounds = simulate_golf_rounds(n_rounds=30)
    end = date.today()
    start = end - timedelta(days=len(rounds) - 1)
    rounds["date"] = pd.date_range(start=start, periods=len(rounds), freq="D")

# 2. Get weather data from API
    weather = fetch_open_meteo(
        lat=40.3356, lon=-75.9269,
        start=start.isoformat(), end=end.isoformat()
    )

# 3. Merge golf and weather data
    merged = rounds.merge(weather, on="date", how="left")
    out = merged.copy()
    out["date"] = out["date"].dt.strftime("%Y-%m-%d")

# Round and clean data
    for col in ["strokes_gained", "tmax", "tmin", "windmax", "tavg"]:
        if col in out.columns:
            out[col] = out[col].round(2)

# I pick wanted columns
    cols = [c for c in ["round", "score", "strokes_gained", "date", "tmax", "tmin", "tavg", "windmax"] if c in out.columns]
    out = out[cols]

# I save as CSV and Excel
    out.to_csv(DATA_PRO / "golf_weather_merged.csv", index=False, sep=";", float_format="%.2f")
    out.to_excel(DATA_PRO / "golf_weather_merged.xlsx", index=False)

# 4. Make charts
    line_scores(rounds)
    scatter_wind_vs_score(merged)

# Run the pipeline
if __name__ == "__main__":
    run_pipeline()

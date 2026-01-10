"""
AgriAssist AI - Phase 1 Data Preprocessing
------------------------------------------
This script ingests Kaggle/manual datasets for:
- Weather
- Soil
- Crop Yield
- Market Prices
- Crop Health (images)

Outputs cleaned datasets ready for predictive modeling.
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import logging

# ---------- CONFIG ----------
DATASET_DIR = os.path.join(os.path.dirname(__file__), "../../datasets")
OUTPUT_DIR = DATASET_DIR

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# ---------- WEATHER DATA ----------
def preprocess_weather(path=os.path.join(DATASET_DIR, "weather.csv"), save=True):
    try:
        df = pd.read_csv(path)
        logging.info(f"Weather dataset loaded: {df.shape[0]} rows, {df.shape[1]} cols")

        df = df.dropna()
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
            df = df.dropna(subset=["date"])

        num_cols = [c for c in ["temperature", "humidity", "rainfall"] if c in df.columns]
        if num_cols:
            scaler = StandardScaler()
            df[num_cols] = scaler.fit_transform(df[num_cols])
            logging.info("Weather features normalized.")

        if save:
            out_path = os.path.join(OUTPUT_DIR, "weather_clean.csv")
            df.to_csv(out_path, index=False)
            logging.info(f"Weather data saved to {out_path}")

        return df
    except Exception as e:
        logging.error(f"Error preprocessing weather data: {e}")
        return pd.DataFrame()

# ---------- SOIL DATA ----------
def preprocess_soil(path=os.path.join(DATASET_DIR, "soil.csv"), save=True):
    try:
        df = pd.read_csv(path)
        logging.info(f"Soil dataset loaded: {df.shape[0]} rows, {df.shape[1]} cols")

        df = df.dropna()
        if "soil_type" in df.columns:
            encoder = LabelEncoder()
            df["soil_type_encoded"] = encoder.fit_transform(df["soil_type"])
            logging.info("Soil types encoded.")

        if save:
            out_path = os.path.join(OUTPUT_DIR, "soil_clean.csv")
            df.to_csv(out_path, index=False)
            logging.info(f"Soil data saved to {out_path}")

        return df
    except Exception as e:
        logging.error(f"Error preprocessing soil data: {e}")
        return pd.DataFrame()

# ---------- CROP YIELD DATA ----------
def preprocess_crop_yield(path=os.path.join(DATASET_DIR, "crop_yield.csv"), save=True):
    try:
        df = pd.read_csv(path)
        logging.info(f"Crop yield dataset loaded: {df.shape[0]} rows, {df.shape[1]} cols")

        df = df.dropna()
        if set(["rainfall", "acreage"]).issubset(df.columns):
            df["rainfall_per_acre"] = df["rainfall"] / df["acreage"].replace(0, np.nan)
            logging.info("Feature engineered: rainfall_per_acre.")

        if save:
            out_path = os.path.join(OUTPUT_DIR, "crop_yield_clean.csv")
            df.to_csv(out_path, index=False)
            logging.info(f"Crop yield data saved to {out_path}")

        return df
    except Exception as e:
        logging.error(f"Error preprocessing crop yield data: {e}")
        return pd.DataFrame()

# ---------- MARKET DATA ----------
def preprocess_market(path=os.path.join(DATASET_DIR, "market_prices.csv"), save=True):
    try:
        df = pd.read_csv(path)
        logging.info(f"Market dataset loaded: {df.shape[0]} rows, {df.shape[1]} cols")

        df = df.dropna()
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
            df = df.dropna(subset=["date"])
        if "crop" in df.columns:
            encoder = LabelEncoder()
            df["crop_encoded"] = encoder.fit_transform(df["crop"])
            logging.info("Crop names encoded.")

        if save:
            out_path = os.path.join(OUTPUT_DIR, "market_prices_clean.csv")
            df.to_csv(out_path, index=False)
            logging.info(f"Market data saved to {out_path}")

        return df
    except Exception as e:
        logging.error(f"Error preprocessing market data: {e}")
        return pd.DataFrame()

# ---------- CROP HEALTH (IMAGE DATA) ----------
def preprocess_crop_health(path=os.path.join(DATASET_DIR, "crop_images/")):
    """
    Placeholder: actual preprocessing will be handled in CNN pipeline.
    Example steps:
    - Resize images to 224x224
    - Normalize pixel values (0-1)
    - Split into train/test sets
    """
    if not os.path.exists(path):
        logging.warning("Crop images folder not found.")
        return None
    logging.info("Crop health preprocessing will be handled in Phase 3 CNN pipeline.")
    return None

# ---------- MAIN ----------
if __name__ == "__main__":
    logging.info("Starting Phase 1 Data Preprocessing...")

    weather = preprocess_weather()
    soil = preprocess_soil()
    crop_yield = preprocess_crop_yield()
    market = preprocess_market()
    crop_health = preprocess_crop_health()

    logging.info("Phase 1 preprocessing complete.")

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ---------- WEATHER DATA ----------
def preprocess_weather(path="datasets/weather.csv", save=True):
    df = pd.read_csv(path)
    df = df.dropna()
    # Convert date column to datetime
    if "date" in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    # Normalize numerical features
    num_cols = [c for c in ["temperature", "humidity", "rainfall"] if c in df.columns]
    if num_cols:
        scaler = StandardScaler()
        df[num_cols] = scaler.fit_transform(df[num_cols])
    if save:
        df.to_csv("datasets/weather_clean.csv", index=False)
    return df

# ---------- SOIL DATA ----------
def preprocess_soil(path="datasets/soil.csv", save=True):
    df = pd.read_csv(path)
    df = df.dropna()
    if "soil_type" in df.columns:
        encoder = LabelEncoder()
        df['soil_type_encoded'] = encoder.fit_transform(df['soil_type'])
    if save:
        df.to_csv("datasets/soil_clean.csv", index=False)
    return df

# ---------- CROP YIELD DATA ----------
def preprocess_crop_yield(path="datasets/crop_yield.csv", save=True):
    df = pd.read_csv(path)
    df = df.dropna()
    if set(["rainfall", "acreage"]).issubset(df.columns):
        df['rainfall_per_acre'] = df['rainfall'] / df['acreage'].replace(0, np.nan)
    if save:
        df.to_csv("datasets/crop_yield_clean.csv", index=False)
    return df

# ---------- MARKET DATA ----------
def preprocess_market(path="datasets/market_prices.csv", save=True):
    df = pd.read_csv(path)
    df = df.dropna()
    if "date" in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    if "crop" in df.columns:
        encoder = LabelEncoder()
        df['crop_encoded'] = encoder.fit_transform(df['crop'])
    if save:
        df.to_csv("datasets/market_prices_clean.csv", index=False)
    return df

# ---------- CROP HEALTH (IMAGE DATA) ----------
def preprocess_crop_health(path="datasets/crop_images/"):
    # Placeholder: actual preprocessing will be handled in CNN training
    # Example: resize images, normalize pixel values
    print("Crop health preprocessing will be handled in CNN pipeline.")
    return None

if __name__ == "__main__":
    print("Preprocessing Weather...")
    weather = preprocess_weather()
    print(weather.head())

    print("Preprocessing Soil...")
    soil = preprocess_soil()
    print(soil.head())

    print("Preprocessing Crop Yield...")
    crop_yield = preprocess_crop_yield()
    print(crop_yield.head())

    print("Preprocessing Market...")
    market = preprocess_market()
    print(market.head())

    print("Crop Health preprocessing will be handled in Phase 3 CNN pipeline.")
